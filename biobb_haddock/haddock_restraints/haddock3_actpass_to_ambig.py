#!/usr/bin/env python3

"""Module containing the haddock  class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger


class Haddock3ActpassToAmbig(BiobbObject):
    """
    | biobb_haddock Haddock3ActpassToAmbig
    | Wrapper class for the Haddock-Restraints active_passive_to_ambig module.
    | `Haddock-Restraints active_passive_to_ambig <https://www.bonvinlab.org/haddock3/clients/haddock.clis.restraints.active_passive_to_ambig.html>`_ generates a corresponding ambig.tbl file to be used by HADDOCK from two given files containing active (in the first line) and passive (second line) residues.

    Args:
        input_actpass1_path (str): Path to the first input HADDOCK active-passive file containing active (in the first line) and passive (second line) residues. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/haddock_actpass1.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), in (edam:format_2330), pass (edam:format_2330).
        input_actpass2_path (str): Path to the second input HADDOCK active-passive file containing active (in the first line) and passive (second line) residues. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/haddock_actpass2.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), in (edam:format_2330), pass (edam:format_2330).
        output_tbl_path (str): Path to the output HADDOCK tbl file with Ambiguous Interaction Restraints (AIR) information. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/haddock_actpass.tbl>`_. Accepted formats: tbl (edam:format_2330), txt (edam:format_2330), out (edam:format_2330).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **pass_to_act** (*bool*) - (False) Path to the haddock haddock executable binary.
            * **segid_one** (*str*) - (None) Segid of the first model.
            * **segid_two** (*str*) - (None) Segid of the second model.
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
            * name: Haddock33-restraints
            * version: 2025.5
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
        self.binary_path = properties.get("binary_path", "haddock3-restraints")
        self.pass_to_act = properties.get("pass_to_act", False)
        self.segid_one = properties.get("segid_one", None)
        self.segid_two = properties.get("segid_two", None)

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3ActpassToAmbig <biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        if self.pass_to_act:
            with open(self.stage_io_dict['in']['input_actpass1_path'], 'r') as file1, \
                    open(self.stage_io_dict['in']['input_actpass2_path'], 'r') as file2:
                actpass1_lines = file1.readlines()
                actpass2_lines = file2.readlines()

            with open(self.stage_io_dict['in']['input_actpass1_path'], 'w') as file1, \
                    open(self.stage_io_dict['in']['input_actpass2_path'], 'w') as file2:
                file1.writelines([actpass1_lines[1], actpass1_lines[0], '\n'])
                file2.writelines([actpass2_lines[1], actpass2_lines[0], '\n'])

        # haddock3-restraints active_passive_to_ambig haddock_actpass.txt
        self.cmd = [self.binary_path, "active_passive_to_ambig", self.stage_io_dict['in']
                    ['input_actpass1_path'], self.stage_io_dict['in']['input_actpass2_path']]

        if self.segid_one is not None:
            self.cmd.extend(["--segid-one", self.segid_one])
        if self.segid_two is not None:
            self.cmd.extend(["--segid-two", self.segid_two])

        self.cmd.append(">")
        self.cmd.append(self.stage_io_dict['out']['output_tbl_path'])
        self.cmd.append("2>&1")

        # Run Biobb block
        self.run_biobb()

        # Remove deprecation warning if present
        with open(self.stage_io_dict['out']['output_tbl_path'], 'r') as file:
            lines = file.readlines()
        if lines and "DEPRECATION NOTICE" in lines[0]:
            with open(self.stage_io_dict['out']['output_tbl_path'], 'w') as file:
                file.writelines(lines[1:])

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
    """Create :class:`Haddock3ActpassToAmbig <biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig>` class and
    execute the :meth:`launch() <biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig.launch>` method."""

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
