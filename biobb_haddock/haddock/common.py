""" Common functions for package biobb_haddock.haddock """
import re
import uuid
import json
import logging
from pathlib import Path
from typing import List, Dict, Mapping, Union, Tuple, Sequence
import biobb_common.tools.file_utils as fu


def create_cfg(output_cfg_path: str, workflow_dict: Mapping[str, str], input_cfg_path: str = None, preset_dict: Mapping[str, str] = None,
               cfg_properties_dict: Mapping[str, str] = None) -> str:
    """Creates an CFG file using the following hierarchy  cfg_properties_dict > input_cfg_path > preset_dict"""
    cfg_dict: Mapping[str, str] = {}

    if preset_dict:
        for k, v in preset_dict.items():
            cfg_dict[k] = v
    if input_cfg_path:
        input_cfg_dict = read_cfg(input_cfg_path)
        for k, v in input_cfg_dict.items():
            cfg_dict[k] = v
    if cfg_properties_dict:
        for k, v in cfg_properties_dict.items():
            cfg_dict[k] = v

    return write_cfg(output_cfg_path, workflow_dict, cfg_dict)


def write_cfg(output_cfg_path: str, workflow_dict: Mapping[str, str], cfg_dict: Mapping[str, str]):
    cfg_list: List[str] = [f"run_dir = '{workflow_dict['run_dir']}'",
                           f"molecules = {workflow_dict['molecules']}",
                           f"\n[{workflow_dict['haddock_step_name']}]"]
    for k, v in cfg_dict.items():
        if isinstance(v, str):
            cfg_list.append(k + ' = ' + f"'{v}'")
        else:
            cfg_list.append(k + ' = ' + str(v))

    with open(output_cfg_path, 'w') as cfg_file:
        for line in cfg_list:
            cfg_file.write(line + '\n')

    return output_cfg_path


def read_cfg(input_mdp_path: str) -> Dict[str, str]:

    # https://github.com/Becksteinlab/GromacsWrapper/blob/master/gromacs/fileformats/mdp.py
    parameter_re = re.compile(r"\s*(?P<parameter>[^=]+?)\s*=\s*(?P<value>[^;]*)(?P<comment>\s*#.*)?", re.VERBOSE)

    cfg_dict: Dict[str, str] = {}
    with open(input_mdp_path) as mdp_file:
        for line in mdp_file:
            re_match = parameter_re.match(line.strip())
            if re_match:
                parameter = re_match.group('parameter')
                value = re_match.group('value')
                cfg_dict[parameter] = value

    return cfg_dict


def cfg_preset(haddock_step_name: str) -> Dict[str, str]:
    cfg_dict = {}
    if not haddock_step_name:
        return cfg_dict

    if haddock_step_name == 'topoaa':
        cfg_dict['autohis'] = True
        cfg_dict['delenph'] = True
        cfg_dict['log_level'] = 'quiet'
        cfg_dict['iniseed'] = 917
        cfg_dict['ligand_param_fname'] = ''
        cfg_dict['ligand_top_fname'] = ''
        cfg_dict['limit'] = True
        cfg_dict['tolerance'] = 0

    return cfg_dict