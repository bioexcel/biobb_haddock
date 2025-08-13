#!/usr/bin/env python3

"""Module containing the haddock  class and the command line interface."""

import os
import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
# from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


class FolderTest(BiobbObject):
    """
    | biobb_haddock FolderTest
    | Wrapper class for the FolderTest module.
    | The FolderTest module.

    Args:
        output_folder (dir): Path of the output folder. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_caprieval.zip>`_. Accepted formats: format (edam:format_1915).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **n** (*int*) - (4) Number of files create.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_haddock.haddock.folder_test import folder_test
            folder_test(output_folder='/path/to/myfiles',
                       properties={'n': 4})

    Info:
        * wrapped_software:
            * name: None
            * version: None
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(
        self,
        output_folder: str,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "out": {"output_folder": output_folder},
        }

        self.n = properties.get('n', 4)
        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`FolderTest <biobb_haddock.haddock.folder_test>` object."""
        # tmp_files = []

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Create n files in the output folder
        sandbox_output_folder = f'{self.stage_io_dict["unique_dir"]}/{self.io_dict["out"]["output_folder"]}'
        os.makedirs(sandbox_output_folder, exist_ok=True)
        for i in range(1, self.n + 1):
            with open(f'{sandbox_output_folder}/file_{i}.txt', 'w') as f:
                f.write(f"This is file number {i}")

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.remove_tmp_files()

        return self.return_code


def folder_test(
    output_folder: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`FolderTest <biobb_haddock.haddock.folder_test>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.folder_test.launch>` method."""

    return FolderTest(
        output_folder=output_folder,
        properties=properties,
        **kwargs,
    ).launch()


folder_test.__doc__ = FolderTest.__doc__


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper of the haddock FolderTest module.",
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
    required_args.add_argument("--output_folder", required=True)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    folder_test(
        output_folder=args.output_folder,
        properties=properties,
    )


if __name__ == "__main__":
    main()
