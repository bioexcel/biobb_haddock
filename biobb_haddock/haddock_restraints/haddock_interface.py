#!/usr/bin/env python3

"""Module containing the haddock class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger


class HaddockRestrainInterface(BiobbObject):
    """
    | biobb_haddock HaddockRestrainInterface
    | Wrapper class for the Haddock-Restraints interface module.
    | `Haddock-Restraints interface <https://www.bonvinlab.org/haddock-restraints/interface.html>`_ lists residues in the interface based on a cutoff distance.

    Args:
        input_pdb_path (str): Path to the input PDB structure to analyze. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/4G6K_clean.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_txt_path (str): Path to the output text file with the list of interface residues. File type: output. Accepted formats: txt (edam:format_2330).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cutoff** (*float*) - (4.0) Cutoff distance in Angstroms for interface residues calculation.
            * **binary_path** (*str*) - ("haddock3-restraints") Path to the HADDOCK3 restraints executable binary.
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

            from biobb_haddock.haddock_restraints.haddock_interface import haddock_interface
            haddock_interface(
                input_pdb_path='/path/to/structure.pdb',
                output_txt_path='/path/to/interface_residues.txt',
                properties={'cutoff': 5.0}
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
        output_txt_path: str,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_pdb_path": input_pdb_path
            },
            "out": {
                "output_txt_path": output_txt_path,
            },
        }

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock-restraints")
        self.cutoff = properties.get("cutoff", 4.0)

        # Check the properties
        self.check_init(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3RestrainInterface <biobb_haddock.haddock_restraints.haddock_interface>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # haddock3-restraints interface <structure> <cutoff>
        self.cmd = [self.binary_path, "interface",
                    self.stage_io_dict['in']['input_pdb_path'],
                    str(self.cutoff)]

        self.cmd.append(">")
        self.cmd.append(self.stage_io_dict['out']['output_txt_path'])
        self.cmd.append("2>&1")

        # Run Biobb block
        self.run_biobb()

        # Open the file and sort the lines so the output is always the same
        with open(self.stage_io_dict['out']['output_txt_path'], 'r') as f:
            lines = f.readlines()
            lines.sort()
        with open(self.stage_io_dict['out']['output_txt_path'], 'w') as f:
            f.writelines(lines)

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.remove_tmp_files()

        return self.return_code


def haddock_interface(
    input_pdb_path: str,
    output_txt_path: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3RestrainInterface <biobb_haddock.haddock_restraints.haddock_interface>` class and
    execute the :meth:`launch() <biobb_haddock.haddock_restraints.haddock_interface.launch>` method."""
    return HaddockRestrainInterface(**dict(locals())).launch()


haddock_interface.__doc__ = HaddockRestrainInterface.__doc__
main = HaddockRestrainInterface.get_main(haddock_interface, "Wrapper of the HADDOCK3 interface module.")


if __name__ == "__main__":
    main()
