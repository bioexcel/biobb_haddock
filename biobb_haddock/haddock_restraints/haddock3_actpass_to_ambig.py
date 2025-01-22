#!/usr/bin/env python3

"""Module containing the haddock  class and the command line interface."""

import argparse
import glob
import os
import shutil
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger


class Haddock3ActpassToAmbig(BiobbObject):
    """
    | biobb_haddock Haddock3ActpassToAmbig
    | Wrapper class for the Haddock-Restraints active_passive_to_ambig module.
    | Haddock-Restraints active_passive_to_ambig generates a corresponding ambig.tbl file to be used by HADDOCK from two given files containing active (in the first line) and passive (second line) residues.

    Args:
        input_actpass1_path (str): Path to the first input HADDOCK active-passive file containing active (in the first line) and passive (second line) residues. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/haddock_actpass.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), in (edam:format_2330), pass (edam:format_2330).
        input_actpass2_path (str): Path to the second input HADDOCK active-passive file containing active (in the first line) and passive (second line) residues. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/haddock_actpass.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), in (edam:format_2330), pass (edam:format_2330).
        output_tbl_path (str): Path to the output HADDOCK tbl file with Ambiguous Interaction Restraints (AIR) information. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/haddock_air.tbl>`_. Accepted formats: tbl (edam:format_2330), txt (edam:format_2330), out (edam:format_2330).
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

            from biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig import haddock3_actpass_to_ambig
            haddock3_actpass_to_ambig(
                input_actpass1_path='/path/to/haddock_actpass1.txt',
                input_actpass2_path='/path/to/haddock_actpass2.txt',
                output_tbl_path='/path/to/output_AIR.tbl'
            )

    Info:
        * wrapped_software:
            * name: Haddock3-restraints
            * version: 3.0.0
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(
        self,
        input_actpass1_path: str,
        input_actpass2_path: str,
        output_tbl_path: str,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_actpass1_path": input_actpass1_path,
                "input_actpass2_path": input_actpass2_path,
            },
            "out": {
                "output_tbl_path": output_tbl_path,
            },
        }

        # Properties specific for BB
        # self.chain = properties.get("chain", "A")

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3-restraints")

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`haddock <haddock.haddock.haddock>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # haddock3-restraints active_passive_to_ambig haddock_actpass.txt
        self.cmd = [self.binary_path, "active_passive_to_ambig", self.stage_io_dict['in']['input_actpass1_path'], self.stage_io_dict['in']['input_actpass2_path']]

        self.cmd.append("&>")
        self.cmd.append(self.stage_io_dict['out']['output_tbl_path'])

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.tmp_files.extend([self.stage_io_dict["unique_dir"]])
        self.remove_tmp_files()

        return self.return_code


def haddock3_actpass_to_ambig(
    input_actpass1_path: str,
    input_actpass2_path: str,
    output_tbl_path: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`haddock <haddock.haddock.haddock>` class and
    execute the :meth:`launch() <haddock.haddock.haddock.launch>` method."""

    return Haddock3ActpassToAmbig(
        input_actpass1_path=input_actpass1_path,
        input_actpass2_path=input_actpass2_path,
        output_tbl_path=output_tbl_path,
        properties=properties,
        **kwargs,
    ).launch()


haddock3_actpass_to_ambig.__doc__ = Haddock3ActpassToAmbig.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock-restraints active_passive_to_ambig module.",
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
    required_args.add_argument("--input_actpass1_path", required=True)
    required_args.add_argument("--input_actpass2_path", required=True)
    required_args.add_argument("--output_tbl_path", required=True)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    haddock3_actpass_to_ambig(
        input_actpass1_path=args.input_actpass1_path,
        input_actpass2_path=args.input_actpass2_path,
        output_tbl_path=args.output_tbl_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
