#!/usr/bin/env python3

"""Module containing the haddock class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger


class Haddock3RestrainBodies(BiobbObject):
    """
    | biobb_haddock Haddock3RestrainBodies
    | Wrapper class for the Haddock-Restraints restrain_bodies module.
    | `Haddock-Restraints restrain_bodies <https://www.bonvinlab.org/haddock3/clients/haddock.clis.restraints.restrain_bodies.html>`_ creates distance restraints to lock several chains together. Useful to avoid unnatural flexibility or movement due to sequence/numbering gaps.

    Args:
        input_structure_path (str): Path to the input PDB structure to be restrained. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/4G6K_clean.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_tbl_path (str): Path to the output HADDOCK tbl file with Ambiguous Interaction Restraints (AIR) information. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/antibody-unambig.tbl>`_. Accepted formats: tbl (edam:format_2330), txt (edam:format_2330), out (edam:format_2330).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **exclude** (*str*) - (None) Chains to exclude from the calculation.
            * **verbose** (*int*) - (0) Tune verbosity of the output.
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

            from biobb_haddock.haddock_restraints.haddock3_restrain_bodies import haddock3_restrain_bodies
            haddock3_restrain_bodies(
                input_structure_path='/path/to/structure.pdb',
                output_tbl_path='/path/to/body_restraints.tbl'
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
        input_structure_path: str,
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
                "input_structure_path": input_structure_path
            },
            "out": {
                "output_tbl_path": output_tbl_path,
            },
        }

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3-restraints")
        self.exclude = properties.get("exclude", None)
        self.verbose = properties.get("verbose", 0)

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3RestrainBodies <biobb_haddock.haddock_restraints.haddock3_restrain_bodies>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # haddock3-restraints restrain_bodies <structure> [--exclude] [--verbose]
        self.cmd = [self.binary_path, "restrain_bodies",
                    self.stage_io_dict['in']['input_structure_path']]

        if self.exclude is not None:
            self.cmd.extend(["--exclude", self.exclude])

        if self.verbose > 0:
            self.cmd.extend(["--verbose", str(self.verbose)])

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


def haddock3_restrain_bodies(
    input_structure_path: str,
    output_tbl_path: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3RestrainBodies <biobb_haddock.haddock_restraints.haddock3_restrain_bodies>` class and
    execute the :meth:`launch() <biobb_haddock.haddock_restraints.haddock3_restrain_bodies.launch>` method."""

    return Haddock3RestrainBodies(
        input_structure_path=input_structure_path,
        output_tbl_path=output_tbl_path,
        properties=properties,
        **kwargs,
    ).launch()


haddock3_restrain_bodies.__doc__ = Haddock3RestrainBodies.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock-restraints restrain_bodies module.",
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
    required_args.add_argument("--input_structure_path", required=True)
    required_args.add_argument("--output_tbl_path", required=True)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    haddock3_restrain_bodies(
        input_structure_path=args.input_structure_path,
        output_tbl_path=args.output_tbl_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
