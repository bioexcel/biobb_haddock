#!/usr/bin/env python3

"""Module containing the Anarcii class and the command line interface."""

import contextlib
import io
import logging
from pathlib import Path
from typing import Optional, Union

from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from anarcii import Anarcii as AnarciiModel


class Anarcii(BiobbObject):
    """
    | biobb_haddock Anarcii
    | Wrapper class for the `ANARCII <https://github.com/oxpig/ANARCII>`_ antibody numbering tool.
    | ANARCII numbers antibody, TCR, and other immune receptor sequences. Given an input PDB structure it renumbers it (IMGT scheme by default) and writes the renumbered PDB structure.

    Args:
        input_pdb_path (str): Path to the input PDB structure file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/4G6K_clean.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_pdb_path (str): Path to the output renumbered PDB structure file. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/utils/4G6K_anarcii_imgt.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **seq_type** (*str*) - ("antibody") Type of sequence to number. Values: antibody, tcr, vhh, sabdab.
            * **mode** (*str*) - ("accuracy") Numbering mode. Values: accuracy, speed.
            * **verbose** (*bool*) - (True) Print verbose output during numbering.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_haddock.utils.anarcii import anarcii
            prop = { 'seq_type': 'antibody',
                     'mode': 'accuracy' }
            anarcii(input_pdb_path='/path/to/structure.pdb',
                    output_pdb_path='/path/to/renumbered.pdb',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: ANARCII
            * version: 2.0.0
            * license: BSD-3-Clause
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(
        self,
        input_pdb_path: Union[str, Path],
        output_pdb_path: Union[str, Path],
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_pdb_path": input_pdb_path},
            "out": {"output_pdb_path": output_pdb_path},
        }

        # Properties specific for BB
        self.seq_type = properties.get("seq_type", "antibody")
        self.mode = properties.get("mode", "accuracy")
        self.verbose = properties.get("verbose", True)

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Anarcii <utils.anarcii.Anarcii>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # ANARCII appends the '.pdb' suffix to the output stem
        output_pdb_path = self.stage_io_dict["out"]["output_pdb_path"]
        pdb_out_stem = str(Path(output_pdb_path).with_suffix(""))

        fu.log(
            "Numbering %s with ANARCII (seq_type=%s, mode=%s)"
            % (self.stage_io_dict["in"]["input_pdb_path"], self.seq_type, self.mode),
            self.out_log,
            self.global_log,
        )

        # Capture ANARCII output (stdout/stderr prints and logging) into the Biobb log
        log_capture = io.StringIO()
        log_handler = logging.StreamHandler(log_capture)
        root_logger = logging.getLogger()
        root_logger.addHandler(log_handler)
        try:
            with contextlib.redirect_stdout(log_capture), contextlib.redirect_stderr(log_capture):
                model = AnarciiModel(
                    seq_type=self.seq_type, mode=self.mode, verbose=self.verbose
                )
                # number() renumbers the structure and returns the numbering
                self.results = model.number(
                    self.stage_io_dict["in"]["input_pdb_path"], pdb_out_stem=pdb_out_stem
                )
        finally:
            root_logger.removeHandler(log_handler)

        captured = log_capture.getvalue().strip()
        if captured:
            fu.log("ANARCII output:\n%s" % captured, self.out_log, self.global_log)

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=True)
        return self.return_code


def anarcii(
    input_pdb_path: Union[str, Path],
    output_pdb_path: Union[str, Path],
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Anarcii <utils.anarcii.Anarcii>` class and
    execute the :meth:`launch() <utils.anarcii.Anarcii.launch>` method."""
    return Anarcii(**dict(locals())).launch()


anarcii.__doc__ = Anarcii.__doc__
main = Anarcii.get_main(anarcii, "Wrapper for the ANARCII antibody numbering tool.")


if __name__ == "__main__":
    main()
