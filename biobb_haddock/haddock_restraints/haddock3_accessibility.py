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


class Haddock3Accessibility(BiobbObject):
    """
    | biobb_haddock Haddock3Accessibility
    | Wrapper class for the Haddock-Restraints Accessibility module.
    | `Haddock-Restraints Accessibility <https://www.bonvinlab.org/haddock3/clients/haddock.clis.restraints.calc_accessibility.html>`_ computes residues accessibility using freesasa included in the Haddock3 package.

    Args:
        input_pdb_path (str): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G_noH.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_accessibility_path (str): Path to the output file with accessibility information. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/mol1_sasa.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), out (edam:format_2330).
        output_actpass_path (str) (Optional): Path to the output file with active/passive residues to be used as haddock3 restraint information. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/mol1_haddock_actpass.txt>`_. Accepted formats: txt (edam:format_2330), dat (edam:format_2330), out (edam:format_2330).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **chain** (*str*) - ("A") Chain to be used from the input PDB file.
            * **cutoff** (*float*) - (0.4) Relative cutoff for sidechain accessibility.
            * **probe_radius** (*float*) - (1.4) Probe radius for the accessibility calculation.
            * **pass_to_act** (*bool*) - (False) If True, the passive residues become active in the actpass file and vice versa.
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

            from biobb_haddock.haddock_restraints.haddock3_accessibility import haddock3_accessibility
            prop = { 'cutoff': 0.4 }
            haddock3_accessibility(input_pdb_path='/path/to/mypdb.pdb',
                       output_accessibility_path='/path/to/output_report.txt',
                       properties=prop)

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
        output_accessibility_path: str,
        output_actpass_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_pdb_path": input_pdb_path,
            },
            "out": {
                "output_accessibility_path": output_accessibility_path,
                "output_actpass_path": output_actpass_path,
            },
        }

        # Properties specific for BB
        self.chain = properties.get("chain", "A")
        self.cutoff = properties.get("cutoff", 0.4)
        self.probe_radius = properties.get("probe_radius", 1.4)
        self.pass_to_act = properties.get("pass_to_act", False)

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3-restraints")

        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3Accessibility <biobb_haddock.haddock_restraints.haddock3_accessibility>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # haddock3-restraints calc_accessibility 1UBQ.pdb --export_to_actpass
        self.cmd = [self.binary_path, "calc_accessibility", self.stage_io_dict['in']['input_pdb_path']]

        if self.io_dict["out"]["output_actpass_path"] is not None:
            self.cmd.append("--export_to_actpass")

        self.cmd.append(f"-c {self.cutoff}")
        self.cmd.append(">")
        self.cmd.append(self.stage_io_dict['out']['output_accessibility_path'])
        self.cmd.append("2>&1")

        # Run Biobb block
        self.run_biobb()

        # Check chain
        target_string = f"Chain {self.chain}"
        found = False
        with open(self.stage_io_dict['out']['output_accessibility_path'], 'r') as file:
            for line in file:
                if target_string in line:
                    found = True

        if found:
            # Rename/Copy output file to the given output file name
            file_name = os.path.basename(self.io_dict['in']['input_pdb_path'])
            shutil.copyfile(f"{file_name[:-4]}_passive_{self.chain}.actpass", self.io_dict["out"]["output_actpass_path"])
            if self.pass_to_act:
                with open(self.io_dict["out"]["output_actpass_path"], 'r') as file:
                    lines = file.readlines()
                with open(self.io_dict["out"]["output_actpass_path"], 'w') as file:
                    file.write(lines[1])
                    file.write('\n\n')
        else:
            print(f"\nWARNING: Chain {self.chain} not found in input PDB file. Please check and modify the chain property accordingly.\n")

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.tmp_files.extend([self.stage_io_dict["unique_dir"]])
        actpass_files = glob.glob('*.actpass')
        self.tmp_files.extend(actpass_files)
        self.remove_tmp_files()

        return self.return_code


def haddock3_accessibility(
    input_pdb_path: str,
    output_accessibility_path: str,
    output_actpass_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3Accessibility <biobb_haddock.haddock_restraints.haddock3_accessibility>` class and
    execute the :meth:`launch() <biobb_haddock.haddock_restraints.haddock3_accessibility.launch>` method."""

    return Haddock3Accessibility(
        input_pdb_path=input_pdb_path,
        output_accessibility_path=output_accessibility_path,
        output_actpass_path=output_actpass_path,
        properties=properties,
        **kwargs,
    ).launch()


haddock3_accessibility.__doc__ = Haddock3Accessibility.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock-restraints Accessibility module.",
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
    required_args.add_argument("--input_pdb_path", required=True)
    required_args.add_argument("--output_accessibility_path", required=True)
    parser.add_argument("--output_actpass_path", required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    haddock3_accessibility(
        input_pdb_path=args.input_pdb_path,
        output_accessibility_path=args.output_accessibility_path,
        output_actpass_path=args.output_actpass_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
