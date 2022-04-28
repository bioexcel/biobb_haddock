#!/usr/bin/env python3

"""Module containing the haddock class and the command line interface."""
import os
import json
import argparse
import shutil
from pathlib import Path
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_haddock.haddock.common import create_haddock_config_file


class Topology(BiobbObject):
    """
    | biobb_haddock Topology
    | Wrapper class for the Haddock Topology module.
    | The  Topology module. haddock haddock module compute classical molecular interaction potentials.

    Args:
        input_pdb_path (str): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/1kim_h.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_pdb_path (str): Path to the output PDB file. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/1kim_neutral.pdb>`_. Accepted formats: pdb (edam:format_1476).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cns_exec** (*str*) - (None) Path to the CNS binary executable path.
            * **ncores** (*int*) - (2) Number of CPU cores to use for the CNS calculations. This will define the number of concurrent jobs being executed. Note that is truncated to the total number of available CPUs minus 1.
            * **autohis** (*bool*) - (True) If set to true, HADDOCK will automatically define the protonation state of histidines ((+1: HIS or 0: HISD/HISE) by selecting the state leading to the lowest electrostatic energy.
            * **delenph** (*bool*) - (True) Since HADDOCK uses a united atom force field, the non-polar hydrogen atoms can be in principle discarded. This saves computing time. However this should not be done if you are defining distance restraints to specific hydrogen atoms (e.g. when using NMR distance restraints).
            * **log_level** (*str*) - ("quiet") CNS, the computational engine used by HADDOCK can generate a lot of output messages. This parameter controls the verbosity of CNS (verbose, normal or quiet).
            * **iniseed** (*int*) - (917) Random seed used in CNS to initialize the random seed function.
            * **ligand_param_fname** (*str*) - (None) Ligand parameter file in CNS format containing all force field parameters (bond, angles, dihedrals, impropers, van der waals) for any ligand not supported by default by HADDOCK.
            * **ligand_top_fname** (*str*) - (None) Ligand topology file in CNS format containing the ligand topologies (atoms, masses, charges, bond definitions...) for any ligand not supported by default by HADDOCK.
            * **limit** (*bool*) - (True) No long description.
            * **tolerance** (*int*) - (0) Percentage of allowed failures for a module to successfully complete.
            * **binary_path** (*str*) - ("haddock") Path to the haddock haddock executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - (None) Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.


    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_haddock.haddock.Topology import topology
            prop = { 'binary_path': 'haddock' }
            topology(input_pdb_path='/path/to/myStructure.pdb',
                     output_pdb_path='/path/to/newStructure.pdb',
                     properties=prop)

    Info:
        * wrapped_software:
            * name: Haddock
            * version: 2.7.0
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(self, input_pdb_path: str, output_pdb_path: str = None, haddock_config_path: str = None,
                 properties: dict = None, **kwargs) -> None:

        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {"input_pdb_path": input_pdb_path, "haddock_config_path": haddock_config_path},
            "out": {"output_pdb_path": output_pdb_path}
        }

        # Properties specific for BB
        self.binary_path = properties.get('binary_path', 'haddock')
        self.autohis = properties.get('autohis', True)



        # Check the properties
        self.check_properties(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`haddock <haddock.haddock.haddock>` object."""
        tmp_files = []

        # Setup Biobb
        if self.check_restart(): return 0

        # Check if output_pdb_path ends with ".pdb" and does not contain underscores
        cfg_properties = {}
        self.haddock_config_path = create_haddock_config_file(cfg_properties)
        self.stage_files()

        # /Users/pau/anaconda3/envs/haddock3/bin/haddock3 /Users/pau/projects/biobb_haddock/biobb_haddock/haddock/haddock_config.cfg

        self.cmd = [self.binary_path,
                    '-i', self.stage_io_dict['in']['combined_params_path'],
                    '-vdw', self.stage_io_dict['in']['input_vdw_params_path'],
                    '-hs', self.stage_io_dict['in']['input_pdb_path']]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # Remove temporal files
        self.tmp_files.extend([self.haddock_config_path])
        self.remove_tmp_files()

        return self.return_code


def topology(input_pdb_path: str,  output_pdb_path: str = None, properties: dict = None, **kwargs) -> int:
    """Create :class:`haddock <haddock.haddock.haddock>` class and
    execute the :meth:`launch() <haddock.haddock.haddock.launch>` method."""

    return Topology(input_pdb_path=input_pdb_path, input_probe_pdb_path=input_probe_pdb_path, output_pdb_path=output_pdb_path,
                    output_grd_path=output_grd_path, output_cube_path=output_cube_path, output_rst_path=output_rst_path,
                    output_byat_path=output_byat_path, output_log_path=output_log_path,
                    input_vdw_params_path=input_vdw_params_path, input_params_path=input_params_path,
                    output_json_box_path=output_json_box_path, input_json_box_path=input_json_box_path,
                    properties=properties, **kwargs).launch()


def main():
    parser = argparse.ArgumentParser(description="Wrapper of the haddock haddock module.",
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_pdb_path', required=True)
    parser.add_argument('--input_probe_pdb_path', required=False)
    parser.add_argument('--output_pdb_path', required=False)
    parser.add_argument('--output_grd_path', required=False)
    parser.add_argument('--output_cube_path', required=False)
    parser.add_argument('--output_rst_path', required=False)
    parser.add_argument('--output_byat_path', required=False)
    parser.add_argument('--output_log_path', required=False)
    parser.add_argument('--input_vdw_params_path', required=False)
    parser.add_argument('--input_params_path', required=False)
    parser.add_argument('--output_json_box_path', required=False)
    parser.add_argument('--input_json_box_path', required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    topology(input_pdb_path=args.input_pdb_path, input_probe_pdb_path=args.input_probe_pdb_path, output_pdb_path=args.output_pdb_path,
             output_grd_path=args.output_grd_path, output_cube_path=args.output_cube_path, output_rst_path=args.output_rst_path,
             output_byat_path=args.output_byat_path, output_log_path=args.output_log_path,
             input_vdw_params_path=args.input_vdw_params_path, input_params_path=args.input_params_path,
             output_json_box_path=args.output_json_box_path, input_json_box_path=args.input_json_box_path,
             properties=properties)


if __name__ == '__main__':
    main()