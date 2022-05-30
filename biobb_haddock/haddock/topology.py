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
from biobb_haddock.haddock.common import create_cfg
from biobb_haddock.haddock.common import cfg_preset


class Topology(BiobbObject):
    """
    | biobb_haddock Topology
    | Wrapper class for the Haddock Topology module.
    | The  Topology module. haddock haddock module compute classical molecular interaction potentials.

    Args:
        mol1_input_pdb_path: (str): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/1kim_h.pdb>`_. Accepted formats: pdb (edam:format_1476).
        mol2_input_pdb_path: (str) (Optional): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/1kim_h.pdb>`_. Accepted formats: pdb (edam:format_1476).
        mol1_output_pdb_path (str): Path to the output PDB file. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/1kim_neutral.pdb>`_. Accepted formats: pdb (edam:format_1476).
        mol2_output_pdb_path (str) (Optional): Path to the output PDB file. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/1kim_neutral.pdb>`_. Accepted formats: pdb (edam:format_1476).
        haddock_wf_data_zip (str) (Optional): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file `
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
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

    def __init__(self, mol1_input_pdb_path: str, mol2_input_pdb_path: str, output_top_zip: str = None, haddock_config_path: str = None,
                 properties: dict = None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = {
            "in": {"mol1_input_pdb_path": mol1_input_pdb_path, "mol2_input_pdb_path": mol2_input_pdb_path, "haddock_config_path": haddock_config_path},
            "out": {"output_top_zip": output_top_zip}
        }

        # Properties specific for BB
        self.haddock_step_name = 'topoaa'
        self.output_cfg_path = properties.get('output_cfg_path', 'haddock.cfg')
        self.cfg = {k: str(v) for k, v in properties.get('cfg', dict()).items()}

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
        self.stage_files()

        workflow_dict = {'run_dir': fu.create_unique_dir(),
                         'molecules': [self.stage_io_dict['in']['mol1_input_pdb_path'], self.stage_io_dict['in']['mol2_input_pdb_path']],
                         'haddock_step_name': self.haddock_step_name}

        # Create data dir
        #os.mkdir(workflow_dict['run_dir']+'/data')
        cfg_dir = fu.create_unique_dir()
        self.output_cfg_path = create_cfg(output_cfg_path=str(Path(cfg_dir).joinpath(self.output_cfg_path)),
                                          workflow_dict=workflow_dict,
                                          input_cfg_path=self.stage_io_dict['in']['haddock_config_path'],
                                          preset_dict=cfg_preset(workflow_dict['haddock_step_name']),
                                          cfg_properties_dict=self.cfg)

        if self.container_path:
            fu.log('Container execution enabled', self.out_log)

            shutil.copy2(self.output_cfg_path, self.stage_io_dict.get("unique_dir"))
            self.output_cfg_path = str(Path(self.container_volume_path).joinpath(Path(self.output_cfg_path).name))


        # /Users/pau/anaconda3/envs/haddock3/bin/haddock3 /Users/pau/projects/biobb_haddock/biobb_haddock/haddock/haddock_config.cfg


        self.cmd = [self.binary_path, self.output_cfg_path]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        # self.copy_to_host()

        # Copy output
        #shutil.copy2(Path(workflow_dict['run_dir'],
        #                  '0_'+self.haddock_step_name,
        #                  str(Path(self.io_dict['in']['input_pdb_path']).stem)+'_haddock.pdb'),
        #             self.io_dict['out']['output_pdb_path'])

        # Create zip output
        fu.log(f"Zipping {workflow_dict['run_dir']} to "
               f"{str(Path(self.io_dict['out']['output_top_zip']).with_suffix(''))} ", self.out_log, self.global_log)
        shutil.make_archive(str(Path(self.io_dict['out']['output_top_zip']).with_suffix('')), 'zip', workflow_dict['run_dir'])

        # Remove temporal files
        self.tmp_files.extend([self.output_cfg_path])
        self.remove_tmp_files()

        return self.return_code


def topology(mol1_input_pdb_path: str, mol2_input_pdb_path: str, output_top_zip: str = None, haddock_config_path: str = None,
             properties: dict = None, **kwargs) -> int:
    """Create :class:`haddock <haddock.haddock.haddock>` class and
    execute the :meth:`launch() <haddock.haddock.haddock.launch>` method."""

    return Topology(mol1_input_pdb_path=mol1_input_pdb_path,
                    mol2_input_pdb_path=mol2_input_pdb_path,
                    output_top_zip=output_top_zip,
                    haddock_config_path=haddock_config_path,
                    properties=properties, **kwargs).launch()


def main():
    parser = argparse.ArgumentParser(description="Wrapper of the haddock haddock module.",
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--mol1_input_pdb_path', required=True)
    required_args.add_argument('--mol2_input_pdb_path', required=True)
    required_args.add_argument('--output_top_zip', required=True)
    parser.add_argument('--haddock_config_path', required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    topology(mol1_input_pdb_path=args.mol1_input_pdb_path,
             mol2_input_pdb_path=args.mol2_input_pdb_path,
             output_top_zip=args.output_top_zip,
             haddock_config_path=args.haddock_config_path,
             properties=properties)


if __name__ == '__main__':
    main()
