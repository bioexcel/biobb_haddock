"""Common functions for package biobb_haddock.haddock"""

import logging
import re
from typing import Any, Optional

import biobb_common.tools.file_utils as fu
from haddock.gear.config import load, save

def create_cfg(
    output_cfg_path: str,
    workflow_dict: dict[str, Any],
    input_cfg_path: Optional[str] = None,
    preset_dict: Optional[dict[str, str]] = None,
    cfg_properties_dict: Optional[dict[str, str]] = None,
    local_log: Optional[logging.Logger] = None,
    global_log: Optional[logging.Logger] = None,
) -> str:
    """Creates an CFG file using the following hierarchy  cfg_properties_dict > input_cfg_path > preset_dict"""
    cfg_dict: dict[str, str] = {}

    if haddock_step_name := workflow_dict.get("haddock_step_name"):
        preset_dict = cfg_preset(haddock_step_name)
        for k, v in preset_dict.items():
            cfg_dict[k] = v
    if input_cfg_path:
        input_cfg_dict = load(input_cfg_path)['final_cfg']
        for k, v in input_cfg_dict.items():
            cfg_dict[k] = v
    if cfg_properties_dict:
        for k, v in cfg_properties_dict.items():
            fu.log("CFG: " + str(k), local_log, global_log)
            fu.log("CFG: " + str(v), local_log, global_log)
            cfg_dict[k] = v
            
    if haddock_step_name:
        cfg_dict = {haddock_step_name: cfg_dict}
    if workflow_dict.get("molecules"):
        cfg_dict["molecules"] = workflow_dict["molecules"]
    if workflow_dict.get("run_dir"):
        cfg_dict["run_dir"] = workflow_dict["run_dir"]
    # Use haddock save
    save(cfg_dict, output_cfg_path)
    
    return output_cfg_path


def cfg_preset(haddock_step_name: str) -> dict[str, Any]:
    cfg_dict: dict[str, Any] = {}
    # cfg_dict["debug"] = True

    if haddock_step_name == "topoaa":
        cfg_dict["autohis"] = True
        cfg_dict["delenph"] = True
        cfg_dict["log_level"] = "quiet"
        cfg_dict["iniseed"] = 917
        cfg_dict["ligand_param_fname"] = ""
        cfg_dict["ligand_top_fname"] = ""
        cfg_dict["limit"] = True
        cfg_dict["tolerance"] = 0

    elif haddock_step_name == "rigidbody":
        cfg_dict["sampling"] = 20
        cfg_dict["tolerance"] = 20

    elif haddock_step_name == "seletop":
        cfg_dict["select"] = 5

    elif haddock_step_name == "flexref":
        cfg_dict["tolerance"] = 20

    elif haddock_step_name == "emref":
        cfg_dict["tolerance"] = 20

    #    elif haddock_step_name == 'seletopclusts':
    #        cfg_dict['select'] = 5

    return cfg_dict


def unzip_workflow_data(zip_file: str, out_log: Optional[logging.Logger] = None) -> str:
    """Extract all files in the zip_file and return the directory.

    Args:
        zip_file (str): Input topology zipball file path.
        out_log (:obj:`logging.Logger`): Input log object.

    Returns:
        str: Path to the extracted directory.

    """
    extract_dir = fu.create_unique_dir()
    zip_list = fu.unzip_list(zip_file, extract_dir, out_log)
    if out_log:
        out_log.info("Unzipping: ")
        out_log.info(zip_file)
        out_log.info("To: ")
        for file_name in zip_list:
            out_log.info(file_name)
    return extract_dir
