#!/usr/bin/env python3

"""Module containing the haddock3 run class and the command line interface."""

# import os
# import json
import argparse
import shutil
from pathlib import Path
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

from biobb_haddock.haddock.common import create_cfg


class Haddock3Run(BiobbObject):
    """
    | biobb_haddock Haddock3Run
    | Wrapper class for the Haddock3 run module.
    | The Haddock3 run module launches the HADDOCK3 execution for docking.

    Args:
        mol1_input_pdb_path (str): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G.pdb>`_. Accepted formats: pdb (edam:format_1476).
        mol2_input_pdb_path (str): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/hpr_ensemble.pdb>`_. Accepted formats: pdb (edam:format_1476).
        ambig_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        unambig_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        hb_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        output_haddock_wf_data_zip (str) (Optional): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip>`_. Accepted formats: zip (edam:format_3987).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
            * **binary_path** (*str*) - ("haddock") Path to the haddock haddock executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - (None) Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.


    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_haddock.haddock.haddock3_run import haddock3_run
            haddock3_run(mol1_input_pdb_path='/path/to/myStructure1.pdb',
                         mol2_input_pdb_path='/path/to/myStructure2.pdb,
                         haddock_config_path='/path/to/myHaddockConfig.cfg',
                         output_haddock_wf_data_zip='/path/to/haddock_output.zip',
                         properties=prop)

    Info:
        * wrapped_software:
            * name: Haddock3
            * version: 2025.5
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(
        self,
        mol1_input_pdb_path: str,
        mol2_input_pdb_path: str,
        output_haddock_wf_data_zip: str,
        ambig_restraints_table_path: Optional[str] = None,
        unambig_restraints_table_path: Optional[str] = None,
        hb_restraints_table_path: Optional[str] = None,
        haddock_config_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {
                "mol1_input_pdb_path": mol1_input_pdb_path,
                "mol2_input_pdb_path": mol2_input_pdb_path,
                "ambig_restraints_table_path": ambig_restraints_table_path,
                "unambig_restraints_table_path": unambig_restraints_table_path,
                "hb_restraints_table_path": hb_restraints_table_path,
                "haddock_config_path": haddock_config_path,

            },
            "out": {
                "output_haddock_wf_data_zip": output_haddock_wf_data_zip,
            },
        }

        # Properties specific for BB
        self.output_cfg_path = properties.get("output_cfg_path", "haddock.cfg")
        self.cfg = {k: str(v)
                    for k, v in properties.get("cfg", dict()).items()}

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3Run <biobb_haddock.haddock.haddock3_run>` object."""
        # tmp_files = []

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        workflow_dict = {
            "run_dir": fu.create_unique_dir(self.stage_io_dict["unique_dir"]),
            "molecules": [self.stage_io_dict["in"]["mol1_input_pdb_path"], self.stage_io_dict["in"]["mol2_input_pdb_path"]],
        }

        if ambig_restraints_table_path := self.stage_io_dict["in"].get("ambig_restraints_table_path"):
            workflow_dict["ambig_restraints_table_path"] = ambig_restraints_table_path
        if unambig_restraints_table_path := self.stage_io_dict["in"].get("unambig_restraints_table_path"):
            workflow_dict["unambig_restraints_table_path"] = unambig_restraints_table_path
        if hb_restraints_table_path := self.stage_io_dict["in"].get("hb_restraints_table_path"):
            workflow_dict["hb_restraints_table_path"] = hb_restraints_table_path

        # Create data dir
        cfg_dir = fu.create_unique_dir(self.stage_io_dict["unique_dir"])
        self.output_cfg_path = create_cfg(
            output_cfg_path=str(Path(cfg_dir).joinpath(self.output_cfg_path)),
            workflow_dict=workflow_dict,
            input_cfg_path=self.stage_io_dict["in"].get("haddock_config_path"),
            cfg_properties_dict=self.cfg,
        )

        if self.container_path:
            fu.log("Container execution enabled", self.out_log)

            shutil.copy2(self.output_cfg_path,
                         self.stage_io_dict.get("unique_dir", ""))
            self.output_cfg_path = str(
                Path(self.container_volume_path).joinpath(
                    Path(self.output_cfg_path).name
                )
            )

        self.cmd = [self.binary_path, self.output_cfg_path]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        # self.copy_to_host()

        # Create zip output
        if self.io_dict["out"].get("output_haddock_wf_data_zip"):
            fu.log(
                f"Zipping {workflow_dict['run_dir']} to {str(Path(self.io_dict['out']['output_haddock_wf_data_zip']).with_suffix(''))} ",
                self.out_log,
                self.global_log,
            )
            shutil.make_archive(
                str(
                    Path(self.io_dict["out"]["output_haddock_wf_data_zip"]).with_suffix(
                        ""
                    )
                ),
                "zip",
                str(workflow_dict["run_dir"]),
            )

        # Remove temporal files
        self.tmp_files.extend([cfg_dir, self.stage_io_dict.get("unique_dir")])
        self.remove_tmp_files()

        return self.return_code


def haddock3_run(
    mol1_input_pdb_path: str,
    mol2_input_pdb_path: str,
    output_haddock_wf_data_zip: str,
    ambig_restraints_table_path: Optional[str] = None,
    unambig_restraints_table_path: Optional[str] = None,
    hb_restraints_table_path: Optional[str] = None,
    haddock_config_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3Run <biobb_haddock.haddock.haddock3_run>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.haddock3_run.launch>` method."""

    return Haddock3Run(
        mol1_input_pdb_path=mol1_input_pdb_path,
        mol2_input_pdb_path=mol2_input_pdb_path,
        output_haddock_wf_data_zip=output_haddock_wf_data_zip,
        ambig_restraints_table_path=ambig_restraints_table_path,
        unambig_restraints_table_path=unambig_restraints_table_path,
        hb_restraints_table_path=hb_restraints_table_path,
        haddock_config_path=haddock_config_path,
        properties=properties,
        **kwargs,
    ).launch()


haddock3_run.__doc__ = Haddock3Run.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock3 HADDOCK3 module.",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(
            prog, width=99999),
    )
    parser.add_argument(
        "-c",
        "--config",
        required=False,
        help="This file can be a YAML file, JSON file or JSON string",
    )

    # Specific args of each building block
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument("--mol1_input_pdb_path", required=True)
    required_args.add_argument("--mol2_input_pdb_path", required=True)
    required_args.add_argument("--output_haddock_wf_data_zip", required=True)
    parser.add_argument("--ambig_restraints_table_path", required=False)
    parser.add_argument("--unambig_restraints_table_path", required=False)
    parser.add_argument("--hb_restraints_table_path", required=False)
    parser.add_argument("--haddock_config_path", required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    haddock3_run(
        mol1_input_pdb_path=args.mol1_input_pdb_path,
        mol2_input_pdb_path=args.mol2_input_pdb_path,
        output_haddock_wf_data_zip=args.output_haddock_wf_data_zip,
        ambig_restraints_table_path=args.ambig_restraints_table_path,
        unambig_restraints_table_path=args.unambig_restraints_table_path,
        hb_restraints_table_path=args.hb_restraints_table_path,
        haddock_config_path=args.haddock_config_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
