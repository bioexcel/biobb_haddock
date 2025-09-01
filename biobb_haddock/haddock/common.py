"""Common functions for package biobb_haddock.haddock"""

import shutil
import logging
import os
import jsonpickle
from pathlib import Path
from typing import Any, Optional
import biobb_common.tools.file_utils as fu
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger
from .haddock3_config import load, save

haddock_2_wf = {
    'ambig_fname': 'ambig_restraints_table_path',
    'unambig_fname': 'unambig_restraints_table_path',
    'hbond_fname': 'hb_restraints_table_path',
}


class HaddockStepBase(BiobbObject):
    """Base class for HADDOCK3 step modules with shared launch functionality."""

    def copy_step_output(
            self, filter_funct: callable,
            output_zip_path: str, sele_top: bool = False) -> None:
        """Copy the output files from the run directory to the output zip path.

        Args:
            obj: The object containing the output paths.
            run_dir (str): The directory where the output files are located.
            filter_funct (callable): A function that accepts a Path and returns True for the files to be copied.
            output_zip_path (str): The path where the output zip file will be created."""
        # Find the directories with the haddock step name
        haddock_output_list = [
            str(path)
            for path in Path(self.run_dir).iterdir()
            if path.is_dir() and str(path).endswith(self.haddock_step_name)
        ]
        # Make the one with the highest step number the first one
        haddock_output_list.sort(reverse=True)
        # Select files with filter_funct
        output_file_list = [
            str(path)
            for path in Path(haddock_output_list[0]).iterdir()
            if path.is_file() and filter_funct(path)
        ]
        if sele_top:
            with open(haddock_output_list[0]+'/io.json') as json_file:
                content = jsonpickle.decode(json_file.read())
                output = content["output"]
            for file in output:
                rel_path = str(file.rel_path).split('/')
                output_file_list.extend(list(Path(self.run_dir+'/'+rel_path[-2]).glob(rel_path[-1]+'*')))
        if len(output_file_list) > 0:
            fu.log("No output files found matching the criteria.", self.out_log, self.global_log)
        fu.zip_list(output_zip_path, output_file_list, self.out_log)

    @launchlogger
    def launch(self) -> int:
        """Execute the HADDOCK step with common workflow."""
        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        if self.stage_io_dict["in"]["input_haddock_wf_data"][-4:] == ".zip":
            # Unzip workflow data to workflow_data_out
            new_input = fu.create_unique_dir(self.stage_io_dict["unique_dir"], '_input_unzipped')
            fu.unzip_list(self.stage_io_dict["in"]["input_haddock_wf_data"], new_input)  # , self.out_log)
            self.stage_io_dict["in"]["input_haddock_wf_data"] = new_input

        self.run_dir = self.stage_io_dict["out"]["output_haddock_wf_data"]
        if self.stage_io_dict["in"]["input_haddock_wf_data"] == self.run_dir:
            shutil.copytree(self.stage_io_dict["in"]["input_haddock_wf_data"],
                            self.run_dir, dirs_exist_ok=True)
        else:
            os.rename(self.stage_io_dict["in"]["input_haddock_wf_data"], self.run_dir)

        workflow_dict = {"haddock_step_name": self.haddock_step_name}
        workflow_dict.update(self.global_cfg)

        # Create workflow configuration
        self.output_cfg_path = create_cfg(
            output_cfg_path=self.create_tmp_file('_haddock.cfg'),
            workflow_dict=workflow_dict,
            input_cfg_path=self.stage_io_dict["in"].get("haddock_config_path"),
            cfg_properties_dict=self.cfg,
        )

        if self.container_path:
            fu.log("Container execution enabled", self.out_log)
            move_to_container_path(self, self.run_dir)

        self.cmd = [self.binary_path, self.output_cfg_path, "--extend-run", self.run_dir]

        # Run Biobb block
        with fu.change_dir(self.run_dir):
            self.run_biobb()

        # Copy files to host
        if hasattr(self, '_handle_step_output'):
            self._handle_step_output()
        if self.io_dict["out"]["output_haddock_wf_data"][-4:] == ".zip":
            zip_wf_output(self, str(workflow_dict["run_dir"]))
        else:
            self.copy_to_host()

        # Remove temporal files
        self.remove_tmp_files()

        return self.return_code


def create_cfg(
    output_cfg_path: str,
    workflow_dict: dict[str, Any],
    input_cfg_path: Optional[str] = None,
    cfg_properties_dict: Optional[dict[str, str]] = None,
    out_log: Optional[logging.Logger] = None,
    global_log: Optional[logging.Logger] = None,
) -> str:
    """Creates an CFG file using the following hierarchy  cfg_properties_dict > input_cfg_path > preset_dict"""
    cfg_dict: dict[str, Any] = {}

    # Handle input configuration if it exists
    if input_cfg_path:
        input_cfg = load(input_cfg_path)
        print(f"Input CFG: {input_cfg}")
        cfg_dict = input_cfg.copy()  # Start with entire loaded config as base

    # Apply single step configuration if specified
    haddock_step_name: str = workflow_dict["haddock_step_name"]
    if not haddock_step_name.startswith("haddock3_"):
        # Get preset properties for this step if any
        step_preset = cfg_preset(haddock_step_name)

        # Create or update the step configuration
        if not cfg_dict:
            # No input config, create new structure with single step
            target_key = haddock_step_name
            cfg_dict = {target_key: step_preset or {}}
        else:
            # Update the specific step in the existing config
            target_key = f"{haddock_step_name}.1"
            if target_key not in cfg_dict:
                cfg_dict[target_key] = {}
            # Merge preset values while preserving existing values
            if step_preset:
                for k, v in step_preset.items():
                    if k not in cfg_dict[target_key]:  # Only add if not already defined
                        cfg_dict[target_key][k] = v

        # Apply custom properties to the step
        if cfg_properties_dict:
            for k, v in cfg_properties_dict.items():
                fu.log(f"CFG: {k} = {v}", out_log, global_log)
                cfg_dict[target_key][k] = v
    # Multiple steps: haddock3_run and haddock3_extend
    else:
        if cfg_properties_dict:
            for key, value in cfg_properties_dict.items():
                if isinstance(value, dict):
                    # If the value is a dictionary, update the corresponding section in cfg_dict
                    if key not in cfg_dict:
                        cfg_dict[key] = {}
                    for sub_key, sub_value in value.items():
                        fu.log(f"CFG: {key}.{sub_key} = {sub_value}", out_log, global_log)
                        cfg_dict[key][sub_key] = sub_value
                else:
                    # If the value is not a dictionary, treat it as a top-level property
                    fu.log(f"CFG: {key} = {value}", out_log, global_log)
                    cfg_dict[key] = value
        # Add workflow_dict properties to cfg_dict
        for key, value in cfg_dict.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    mapped_key = haddock_2_wf.get(sub_key)
                    if mapped_key and mapped_key in workflow_dict:
                        sub_value = workflow_dict[mapped_key]
                        cfg_dict[key][sub_key] = sub_value

    # Add molecules and run_dir if provided
    for key, value in workflow_dict.items():
        fu.log(f"CFG: {key} = {value}", out_log, global_log)
        if key == 'haddock_step_name' or key in haddock_2_wf.values():
            continue
        cfg_dict[key] = value

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

    return cfg_dict


def move_to_container_path(obj, run_dir=None):
    """Move configuration and run directory to container path."""
    shutil.copy2(obj.output_cfg_path, obj.stage_io_dict.get("unique_dir", ""))
    obj.output_cfg_path = str(
        Path(obj.container_volume_path).joinpath(
            Path(obj.output_cfg_path).name
        )
    )
    if run_dir:
        shutil.copytree(
            run_dir,
            str(
                Path(obj.stage_io_dict.get("unique_dir", "")).joinpath(
                    Path(run_dir).name
                )
            ),
        )
        run_dir = str(Path(obj.stage_io_dict.get("unique_dir", "")).joinpath(Path(run_dir).name))


def zip_wf_output(obj):
    """Zip all the files in the run directory and save it to the output path."""
    fu.log(
        f"Zipping {obj.run_dir} to {str(Path(obj.io_dict['out']['output_haddock_wf_data']).with_suffix(''))} ",
        obj.out_log, obj.global_log)

    shutil.make_archive(
        str(Path(obj.io_dict["out"]["output_haddock_wf_data"]).with_suffix("")),
        "zip", obj.run_dir)
