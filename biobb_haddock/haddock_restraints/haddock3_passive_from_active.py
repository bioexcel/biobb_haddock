#!/usr/bin/env python3

"""Module containing the Haddock3PassiveFromActive class and the command line interface."""

import re
from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu


class Haddock3PassiveFromActive(BiobbObject):
    """
    | biobb_haddock Haddock3PassiveFromActive
    | Wrapper class for the Haddock3-Restraints passive_from_active module.
    | `Haddock3-Restraints passive_from_active <https://www.bonvinlab.org/haddock3-user-manual/restraints_cli.html#passive-from-active>`_ given a list of active_residues and a PDB structure, it will return a list of surface exposed passive residues within a radius (6.5Å by default) from the active residues.

    Args:
        input_pdb_path (str): Path to the input PDB structure file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/1A2P_ch.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_actpass_path (str): Path to the output file with list of passive residues. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/1A2P_manual_actpass.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), list (edam:format_2330), out (edam:format_2330).
        input_active_list_path (str) (Optional): Path to the input file with the active residue numbers, separated by commas, spaces or new lines. File type: input. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), list (edam:format_2330).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **active_list** (*str*) - ('') List of active residues as a comma-separated string. Required if input_active_list_path is not provided.
            * **chain_id** (*str*) - (None) Chain ID to consider when calculating passive residues.
            * **surface_list_path** (*str*) - ("") Path to a file with the surface residue numbers to consider, separated by commas, spaces or new lines.
            * **radius** (*float*) - (6.5) Radius in Angstroms to look for surface residues around active ones.
            * **binary_path** (*str*) - ("haddock3-restraints") Path to the haddock3-restraints executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - (None) Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
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
            * name: Haddock3-restraints
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
        super().__init__(**locals())

    def prepare(self) -> None:
        """Check that the active residues are given."""
        if not self.io_dict["in"].get("input_active_list_path") and not self.active_list:
            raise ValueError("Either input_active_list_path or active_list property must be provided")

    def run(self) -> None:
        """Execute the :class:`Haddock3PassiveFromActive <biobb_haddock.haddock_restraints.haddock3_passive_from_active>` object."""
        active_list = self.active_list
        if self.io_dict["in"].get("input_active_list_path"):
            with open(self.sandbox_file("input_active_list_path")) as active_file:
                active_list = comma_list(active_file.read())

        # Build command line
        # haddock3-restraints passive_from_active <pdb_file> <active_list> [-c <chain_id>] [-s <surface_list>] [-r <radius>]
        self.cmd = [
            self.binary_path,
            "passive_from_active",
            self.stage_io_dict['in']['input_pdb_path'],
            f"\"{active_list}\""
        ]

        # Add optional parameters
        if self.chain_id:
            self.cmd.extend(["-c", self.chain_id])

        if self.surface_list_path:
            with open(self.surface_list_path) as surface_file:
                self.cmd.extend(["-s", comma_list(surface_file.read())])

        self.cmd.extend(["-r", str(self.radius)])

        # Redirect only stdout (the result): stderr (warnings, errors) goes to the error log
        self.cmd.append(">")
        self.cmd.append(self.stage_io_dict['out']['output_actpass_path'])

        # Run Biobb block
        self.run_biobb()

        # Remove deprecation warning if present
        with open(self.sandbox_file("output_actpass_path"), 'r') as file:
            lines = file.readlines()
        fu.log('Result: ' + '\n'.join(lines), self.out_log, self.global_log)
        with open(self.sandbox_file("output_actpass_path"), 'w') as file:
            file.write(active_list.replace(",", " ")+"\n")
            if lines and "DEPRECATION NOTICE" in lines[0]:
                file.writelines(lines[1:])
            else:
                file.writelines(lines)


def comma_list(text: str) -> str:
    """Go from residue numbers separated by commas, spaces or new lines to a comma-separated list."""
    return ",".join(number for number in re.split(r"[\s,]+", text) if number)


haddock3_passive_from_active = launcher(Haddock3PassiveFromActive)


if __name__ == "__main__":
    Haddock3PassiveFromActive.main()
