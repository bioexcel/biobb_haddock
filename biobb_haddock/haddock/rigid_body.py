#!/usr/bin/env python3

"""Module containing the haddock RigidBody class and the command line interface."""

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

from biobb_haddock.haddock.common import create_cfg, unzip_workflow_data


class RigidBody(BiobbObject):
    """
    | biobb_haddock RigidBody
    | Wrapper class for the Haddock RigidBody module.
    | The RigidBody module. `Haddock RigidBody module <https://www.bonvinlab.org/haddock3/modules/sampling/haddock.modules.sampling.rigidbody.html>`_ compute rigid body docking between two molecules.

    Args:
        input_haddock_wf_data_zip (str): Path to the input zipball containing all the current Haddock workflow data. File type: input. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip>`_. Accepted formats: zip (edam:format_3987).
        docking_output_zip_path (str): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip>`_. Accepted formats: zip (edam:format_3987).
        ambig_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        unambig_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        hb_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        output_haddock_wf_data_zip (str) (Optional): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip>`_. Accepted formats: zip (edam:format_3987).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
            * **global_cfg** (*dict*) - ({"postprocess": False}) `Global configuration options <https://www.bonvinlab.org/haddock3-user-manual/global_parameters.html>`_ specification.
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

            from biobb_haddock.haddock.rigid_body import rigid_body
            prop = { 'binary_path': 'haddock' }
            rigid_body(input_haddock_wf_data_zip='/path/to/myworkflowdata.zip',
                       docking_output_zip_path='/path/to/mydockingstructures.zip',
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
        input_haddock_wf_data_zip: str,
        docking_output_zip_path: str,
        ambig_restraints_table_path: Optional[str] = None,
        unambig_restraints_table_path: Optional[str] = None,
        hb_restraints_table_path: Optional[str] = None,
        output_haddock_wf_data_zip: Optional[str] = None,
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
                "ambig_restraints_table_path": ambig_restraints_table_path,
                "unambig_restraints_table_path": unambig_restraints_table_path,
                "hb_restraints_table_path": hb_restraints_table_path,
                "haddock_config_path": haddock_config_path,
            },
            "out": {
                "output_haddock_wf_data_zip": output_haddock_wf_data_zip,
                "docking_output_zip_path": docking_output_zip_path,
            },
        }
        # Should not be copied inside container
        self.input_haddock_wf_data_zip = input_haddock_wf_data_zip

        # Properties specific for BB
        self.haddock_step_name = "rigidbody"
        self.output_cfg_path = properties.get("output_cfg_path", "haddock.cfg")
        # self.cfg = {k: str(v) for k, v in properties.get('cfg', dict()).items()}
        self.cfg = {k: v for k, v in properties.get("cfg", dict()).items()}
        self.global_cfg = properties.get("global_cfg", dict(postprocess=False))

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`RigidBody <biobb_haddock.haddock.rigid_body>` object."""
        # tmp_files = []

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Unzip workflow data to workflow_data_out
        run_dir = unzip_workflow_data(
            zip_file=self.input_haddock_wf_data_zip, out_log=self.out_log
        )

        workflow_dict = {"haddock_step_name": self.haddock_step_name}
        workflow_dict.update(self.global_cfg)

        if ambig_path := self.stage_io_dict["in"].get("ambig_restraints_table_path"):
            self.cfg["ambig_fname"] = ambig_path

        if unambig_fname := self.stage_io_dict["in"].get("unambig_restraints_table_path"):
            self.cfg["unambig_fname"] = unambig_fname

        if hbond_fname := self.stage_io_dict["in"].get("hb_restraints_table_path"):
            self.cfg["hbond_fname"] = hbond_fname

        # Create data dir
        cfg_dir = fu.create_unique_dir()
        self.output_cfg_path = create_cfg(
            output_cfg_path=str(Path(cfg_dir).joinpath(self.output_cfg_path)),
            workflow_dict=workflow_dict,
            input_cfg_path=self.stage_io_dict["in"].get("haddock_config_path"),
            cfg_properties_dict=self.cfg,
            local_log=self.out_log,
            global_log=self.global_log,
        )

        if self.container_path:
            fu.log("Container execution enabled", self.out_log)

            shutil.copy2(self.output_cfg_path, self.stage_io_dict.get("unique_dir", ""))
            self.output_cfg_path = str(
                Path(self.container_volume_path).joinpath(
                    Path(self.output_cfg_path).name
                )
            )

            shutil.copytree(
                run_dir,
                str(
                    Path(self.stage_io_dict.get("unique_dir", "")).joinpath(
                        Path(run_dir).name
                    )
                ),
            )
            run_dir = str(
                Path(self.stage_io_dict.get("unique_dir", "")).joinpath(
                    Path(run_dir).name
                )
            )

        self.cmd = [self.binary_path, self.output_cfg_path, "--extend-run", run_dir]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        # self.copy_to_host()

        # Copy output

        haddock_output_list = [
            str(path)
            for path in Path(run_dir).iterdir()
            if path.is_dir() and str(path).endswith(workflow_dict["haddock_step_name"])
        ]
        haddock_output_list.sort(reverse=True)
        output_file_list = list(
            Path(haddock_output_list[0]).glob(
                workflow_dict["haddock_step_name"] + r"*.pdb*"
            )
        )
        fu.zip_list(
            self.io_dict["out"]["docking_output_zip_path"],
            output_file_list,
            self.out_log,
        )

        # Create zip output
        if self.io_dict["out"].get("output_haddock_wf_data_zip"):
            fu.log(
                f"Zipping {run_dir} to {str(Path(self.io_dict['out']['output_haddock_wf_data_zip']).with_suffix(''))} ",
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
                run_dir,
            )

        # Remove temporal files
        self.tmp_files.extend([
            run_dir,
            cfg_dir,
            self.stage_io_dict.get("unique_dir")])
        self.remove_tmp_files()

        return self.return_code


def rigid_body(
    input_haddock_wf_data_zip: str,
    docking_output_zip_path: str,
    ambig_restraints_table_path: Optional[str] = None,
    unambig_restraints_table_path: Optional[str] = None,
    hb_restraints_table_path: Optional[str] = None,
    output_haddock_wf_data_zip: Optional[str] = None,
    haddock_config_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`RigidBody <biobb_haddock.haddock.rigid_body>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.rigid_body.launch>` method."""

    return RigidBody(
        input_haddock_wf_data_zip=input_haddock_wf_data_zip,
        docking_output_zip_path=docking_output_zip_path,
        ambig_restraints_table_path=ambig_restraints_table_path,
        unambig_restraints_table_path=unambig_restraints_table_path,
        hb_restraints_table_path=hb_restraints_table_path,
        output_haddock_wf_data_zip=output_haddock_wf_data_zip,
        haddock_config_path=haddock_config_path,
        properties=properties,
        **kwargs,
    ).launch()


rigid_body.__doc__ = RigidBody.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock RigidBody module.",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999),
    )
    parser.add_argument(
        "-c",
        "--config",
        required=False,
        help="This file can be a YAML file, JSON file or JSON string",
    )

    # Specific args of each building block
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument("--input_haddock_wf_data_zip", required=True)
    required_args.add_argument("--docking_output_zip_path", required=True)
    parser.add_argument("--ambig_restraints_table_path", required=False)
    parser.add_argument("--unambig_restraints_table_path", required=False)
    parser.add_argument("--hb_restraints_table_path", required=False)
    parser.add_argument("--output_haddock_wf_data_zip", required=False)
    parser.add_argument("--haddock_config_path", required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    rigid_body(
        input_haddock_wf_data_zip=args.input_haddock_wf_data_zip,
        docking_output_zip_path=args.docking_output_zip_path,
        ambig_restraints_table_path=args.restraints_table_path,
        unambig_restraints_table_path=args.restraints_table_path,
        hb_restraints_table_path=args.restraints_table_path,
        output_haddock_wf_data_zip=args.output_haddock_wf_data_zip,
        haddock_config_path=args.haddock_config_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
