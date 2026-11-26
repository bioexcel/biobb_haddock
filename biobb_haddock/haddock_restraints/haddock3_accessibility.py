#!/usr/bin/env python3

"""Module containing the haddock  class and the command line interface."""

import os
import re
import shutil
from typing import Optional

from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu

# calc_accessibility writes its report as Python log records, e.g.
# "16/11/2026 12:49:38 L227 INFO - Chain: A - 150 residues"
REPORT_RECORD = re.compile(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} L\d+ [A-Z]+ - ")


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
            * **binary_path** (*str*) - ("haddock3-restraints") Path to the haddock haddock executable binary.
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

            from biobb_haddock.haddock_restraints.haddock3_accessibility import haddock3_accessibility
            prop = { 'cutoff': 0.4 }
            haddock3_accessibility(input_pdb_path='/path/to/mypdb.pdb',
                       output_accessibility_path='/path/to/output_report.txt',
                       properties=prop)

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
        output_accessibility_path: str,
        output_actpass_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`Haddock3Accessibility <biobb_haddock.haddock_restraints.haddock3_accessibility>` object."""

        # haddock3-restraints calc_accessibility 1UBQ.pdb --export_to_actpass
        self.cmd = [self.binary_path, "calc_accessibility", self.stage_io_dict['in']['input_pdb_path']]

        if self.io_dict["out"]["output_actpass_path"] is not None:
            self.cmd.append("--export_to_actpass")

        self.cmd.append(f"-c {self.cutoff}")
        # calc_accessibility writes its report with Python logging, i.e. to stderr,
        # so here stderr (not stdout) is redirected to the report file
        self.cmd.append("2>")
        self.cmd.append(self.stage_io_dict['out']['output_accessibility_path'])

        # Run Biobb block
        self.run_biobb()

        # Keep only the tool's log records in the report: any other stderr
        # line (e.g. Python warnings, tracebacks) goes to the error log
        report_path = self.sandbox_file("output_accessibility_path")
        with open(report_path, 'r') as file:
            lines = file.readlines()
        other_lines = [line for line in lines if not REPORT_RECORD.match(line)]
        if other_lines:
            fu.log(''.join(other_lines), self.err_log)
            with open(report_path, 'w') as file:
                file.writelines(line for line in lines if REPORT_RECORD.match(line))

        # Check chain
        target_string = f"Chain {self.chain}"
        found = False
        with open(self.sandbox_file("output_accessibility_path"), 'r') as file:
            for line in file:
                if target_string in line:
                    found = True

        if found:
            # Rename/Copy output file to the given output file name: the tool writes it in the sandbox
            file_name = os.path.basename(self.io_dict['in']['input_pdb_path'])
            shutil.copyfile(os.path.join(self.stage_io_dict["unique_dir"], f"{file_name[:-4]}_passive_{self.chain}.actpass"),
                            self.sandbox_file("output_actpass_path"))
            if self.pass_to_act:
                with open(self.sandbox_file("output_actpass_path"), 'r') as file:
                    lines = file.readlines()
                with open(self.sandbox_file("output_actpass_path"), 'w') as file:
                    file.write(lines[1])
                    file.write('\n\n')
        else:
            print(f"\nWARNING: Chain {self.chain} not found in input PDB file. Please check and modify the chain property accordingly.\n")


haddock3_accessibility = launcher(Haddock3Accessibility)


if __name__ == "__main__":
    Haddock3Accessibility.main()
