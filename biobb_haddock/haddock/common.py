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
    cfg_dict = {}

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
    pass
