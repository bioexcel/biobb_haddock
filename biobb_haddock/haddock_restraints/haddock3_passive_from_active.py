#!/usr/bin/env python3

"""Module containing the Haddock3PassiveFromActive class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger
from biobb_common.tools import file_utils as fu


class Haddock3PassiveFromActive(BiobbObject):
    """
    | biobb_haddock Haddock3PassiveFromActive
    | Wrapper class for the Haddock3-Restraints passive_from_active module.
    | `Haddock3-Restraints passive_from_active <https://www.bonvinlab.org/haddock3/clients/haddock.clis.restraints.passive_from_active.html>`_ given a list of active_residues and a PDB structure, it will return a list of surface exposed passive residues within a radius (6.5Å by default) from the active residues.

    Args:
        input_pdb_path (str): Path to the input PDB structure file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/1A2P_ch.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_actpass_path (str): Path to the output file with list of passive residues. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/1A2P_manual_actpass.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), list (edam:format_2330), out (edam:format_2330).
        input_active_list_path (str) (Optional): Path to the input file with list of active residues. File type: input. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), list (edam:format_2330).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **active_list** (*str*) - ('') List of active residues as a comma-separated string. Required if input_active_list_path is not provided.
            * **chain_id** (*str*) - (None) Chain ID to consider when calculating passive residues.
            * **surface_list_path** (*str*) - ("") Path to file with list of surface residues to filter.
            * **radius** (*float*) - (6.5) Radius in Angstroms to look for surface residues around active ones.
            * **binary_path** (*str*) - ("haddock3-restraints") Path to the haddock3-restraints executable binary.
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

            from biobb_haddock.haddock_restraints.haddock3_passive_from_active import haddock3_passive_from_active
            haddock3_passive_from_active(
                input_pdb_path='/path/to/structure.pdb',
                input_active_list_path='/path/to/active_residues.txt',
                output_actpass_path='/path/to/actpass.tbl.txt',
                properties={
                    'chain_id': 'A',
                    'radius': 6.5
                }
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
        input_pdb_path: str,
        output_actpass_path: str,
        input_active_list_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_pdb_path": input_pdb_path
            },
            "out": {
                "output_actpass_path": output_actpass_path
            },
        }

        # Add input_active_list_path to io_dict if provided
        if input_active_list_path:
            self.io_dict["in"]["input_active_list_path"] = input_active_list_path

        # Properties specific for BB
        self.active_list = properties.get("active_list", "")
        self.chain_id = properties.get("chain_id", None)
        self.surface_list_path = properties.get("surface_list_path", "")
        self.radius = properties.get("radius", 6.5)
        self.binary_path = properties.get("binary_path", "haddock3-restraints")

        # Check that either input_active_list_path or active_list is provided
        if not input_active_list_path and not self.active_list:
            raise ValueError(
                "Either input_active_list_path or active_list property must be provided")

        # Check the properties
        self.check_properties(properties)

        # If surface_list_path is provided overwrite the active_list
        if self.surface_list_path:
            with open(self.surface_list_path, "r") as surface_file:
                self.active_list = surface_file.read()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3PassiveFromActive <biobb_haddock.haddock_restraints.haddock3_passive_from_active>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Build command line
        # haddock3-restraints passive_from_active <pdb_file> <active_list> [-c <chain_id>] [-s <surface_list>] [-r <radius>]
        self.cmd = [
            self.binary_path,
            "passive_from_active",
            self.stage_io_dict['in']['input_pdb_path'],
            self.active_list
        ]

        # Add optional parameters
        if self.chain_id:
            self.cmd.extend(["-c", self.chain_id])

        if self.surface_list_path:
            self.cmd.extend(
                ["-s", self.stage_io_dict['in']['surface_list_path']])

        # Radius not in this version
        # self.cmd.extend(["-r", str(self.radius)])

        # Redirect output to the output file
        self.cmd.append(">")
        self.cmd.append(self.stage_io_dict['out']['output_actpass_path'])
        self.cmd.append("2>&1")

        # Run Biobb block
        self.run_biobb()

        # Remove deprecation warning if present
        with open(self.stage_io_dict['out']['output_actpass_path'], 'r') as file:
            lines = file.readlines()
        fu.log('Result: ' + '\n'.join(lines), self.out_log, self.global_log)
        with open(self.stage_io_dict['out']['output_actpass_path'], 'w') as file:
            file.write(self.active_list.replace(",", " ")+"\n")
            if lines and "DEPRECATION NOTICE" in lines[0]:
                file.writelines(lines[1:])
            else:
                file.writelines(lines)

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.tmp_files.extend([self.stage_io_dict["unique_dir"]])
        self.remove_tmp_files()

        return self.return_code


def haddock3_passive_from_active(
    input_pdb_path: str,
    output_actpass_path: str,
    input_active_list_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3PassiveFromActive <biobb_haddock.haddock_restraints.haddock3_passive_from_active>` class and
    execute the :meth:`launch() <biobb_haddock.haddock_restraints.haddock3_passive_from_active.launch>` method."""

    return Haddock3PassiveFromActive(
        input_pdb_path=input_pdb_path,
        output_actpass_path=output_actpass_path,
        input_active_list_path=input_active_list_path,
        properties=properties,
        **kwargs,
    ).launch()


haddock3_passive_from_active.__doc__ = Haddock3PassiveFromActive.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock3-restraints passive_from_active module.",
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
    required_args.add_argument("--input_pdb_path", required=True)
    required_args.add_argument("--output_actpass_path", required=True)

    # Optional arguments
    parser.add_argument("--input_active_list_path", required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    haddock3_passive_from_active(
        input_pdb_path=args.input_pdb_path,
        output_actpass_path=args.output_actpass_path,
        input_active_list_path=args.input_active_list_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
