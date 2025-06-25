#!/usr/bin/env python3

"""Module containing the haddock3 run class and the command line interface."""

import argparse
import zipfile
import shutil
from pathlib import Path
from typing import Optional
import os
from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


class Haddock3Extend(BiobbObject):
    """
    | biobb_haddock Haddock3Extend
    | Wrapper class for the Haddock3 extend module.
    | The `Haddock3 extend <https://www.bonvinlab.org/haddock3/tutorials/continuing_runs.html>`_. module continues the HADDOCK3 execution for docking of an already started run.

    Args:
        input_haddock_wf_data_zip (str): Path to the input zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip>`_. Accepted formats: zip (edam:format_3987).
        haddock_config_path (str): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        output_haddock_wf_data_zip (str): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
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

            from biobb_haddock.haddock.haddock3_extend import haddock3_extend
            haddock3_extend(input_haddock_wf_data_zip='/path/to/myworkflowdata.zip',
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
        input_haddock_wf_data_zip: str,
        haddock_config_path: str,
        output_haddock_wf_data_zip: str,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_haddock_wf_data_zip": input_haddock_wf_data_zip,
                "haddock_config_path": haddock_config_path,
            },
            "out": {
                "output_haddock_wf_data_zip": output_haddock_wf_data_zip,
            },
        }

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3Extend <biobb_haddock.haddock.haddock3_extend>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Decompress input zip
        run_dir = fu.create_unique_dir(self.stage_io_dict["unique_dir"])
        with zipfile.ZipFile(self.stage_io_dict["in"]["input_haddock_wf_data_zip"], 'r') as zip_ref:
            zip_ref.extractall(run_dir)
        cwd = os.getcwd()
        # Move the unzip folder
        os.chdir(run_dir)

        if self.container_path:
            fu.log("Container execution enabled", self.out_log)

            shutil.copy2(self.output_cfg_path, self.stage_io_dict.get("unique_dir", ""))
            self.output_cfg_path = str(
                Path(self.container_volume_path).joinpath(
                    Path(self.output_cfg_path).name
                )
            )

        self.cmd = [self.binary_path, self.stage_io_dict["in"]["haddock_config_path"]]
        self.cmd.extend(["--extend-run", run_dir])

        # Run Biobb block
        self.run_biobb()
        # Move back to the stage directory
        os.chdir(cwd)
        # Create zip output
        fu.log(
            f"Zipping {run_dir} to {str(Path(self.io_dict['out']['output_haddock_wf_data_zip']).with_suffix(''))} ",
            self.out_log, self.global_log)
        shutil.make_archive(
            str(Path(self.io_dict["out"]["output_haddock_wf_data_zip"]).with_suffix("")),
            "zip",
            str(run_dir),
        )

        # Remove temporal files
        self.tmp_files.extend([self.stage_io_dict.get("unique_dir"), run_dir])
        self.remove_tmp_files()

        return self.return_code


def haddock3_extend(
    input_haddock_wf_data_zip: str,
    haddock_config_path: str,
    output_haddock_wf_data_zip: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3Extend <biobb_haddock.haddock.haddock3_extend>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.haddock3_extend.launch>` method."""

    return Haddock3Extend(
        input_haddock_wf_data_zip=input_haddock_wf_data_zip,
        haddock_config_path=haddock_config_path,
        output_haddock_wf_data_zip=output_haddock_wf_data_zip,
        properties=properties,
        **kwargs,
    ).launch()


haddock3_extend.__doc__ = Haddock3Extend.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock3 HADDOCK3 module.",
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
    required_args.add_argument("--haddock_config_path", required=True)
    required_args.add_argument("--output_haddock_wf_data_zip", required=True)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    haddock3_extend(
        input_haddock_wf_data_zip=args.input_haddock_wf_data_zip,
        haddock_config_path=args.haddock_config_path,
        output_haddock_wf_data_zip=args.output_haddock_wf_data_zip,
        properties=properties,
    )


if __name__ == "__main__":
    main()
