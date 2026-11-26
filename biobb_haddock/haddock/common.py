"""Common functions for package biobb_haddock.haddock"""

import shutil
import logging
import os
import re
import jsonpickle
from pathlib import Path
from typing import Any, ClassVar, Iterable, Optional
import biobb_common.tools.file_utils as fu
from biobb_common.generic.biobb_object import BiobbObject
from .haddock3_config import load, save

haddock_2_wf = {
    'ambig_fname': 'ambig_restraints_table_path',
    'unambig_fname': 'unambig_restraints_table_path',
    'hbond_fname': 'hb_restraints_table_path',
}


# Restraint tables of the docking and refinement steps: {argument: HADDOCK3 parameter}
RESTRAINT_FILES = {
    "ambig_restraints_table_path": "ambig_fname",
    "unambig_restraints_table_path": "unambig_fname",
    "hb_restraints_table_path": "hbond_fname",
}


class HaddockStepBase(BiobbObject):
    """Base class of the HADDOCK3 blocks: they run a step (or a whole run) on the workflow data of the input
    folder. The blocks set the class attributes."""

    # HADDOCK3 module of the step, ie: "rigidbody"
    haddock_step_name: ClassVar[str]
    # Input files given in the configuration of the step: {argument: HADDOCK3 parameter}
    cfg_files: ClassVar[dict[str, str]] = {}
    # Output zip argument with the files of the step folder that match the step_zip_files patterns
    step_zip: ClassVar[Optional[str]] = None
    step_zip_files: ClassVar[tuple[str, ...]] = ("*",)
    # The step zip also has the models that the step selected from the folders of the previous steps
    zip_selected_models: ClassVar[bool] = False

    def write_cfg(self, **workflow: Any) -> None:
        """Go from the haddock_config_path file, the cfg and global_cfg properties, the cfg_files inputs and
        **workflow** (ie: run_dir, molecules) to the HADDOCK3 configuration of the step: output_cfg_path."""
        cfg = dict(self.cfg)
        for argument, parameter in self.cfg_files.items():
            if self.io_dict["in"].get(argument):
                cfg[parameter] = self.run_path(self.sandbox_file(argument))
        self.output_cfg_path = create_cfg(
            output_cfg_path=self.create_tmp_file('_haddock.cfg'),
            workflow_dict={"haddock_step_name": self.haddock_step_name, **workflow, **self.global_cfg},
            input_cfg_path=self.sandbox_file("haddock_config_path"),
            properties_cfg_dict=cfg,
            out_log=self.out_log,
            global_log=self.global_log,
        )

    def zip_step_files(self, argument: str, patterns: Iterable[str], selected_models: bool = False) -> None:
        """Go from the step folder of the run folder (the last one of the module) to the **argument** output zip:
        its files that match **patterns** (io.json and params.cfg excluded) and, with **selected_models**, the
        models the step selected. Nothing if the optional output is not given."""
        zip_path = self.sandbox_file(argument)
        if not zip_path:
            return
        steps = {number: name for (number, module), name in step_folders(Path(self.run_dir)).items()
                 if module == self.haddock_step_name}
        if not steps:
            fu.log(f"No {self.haddock_step_name} step folder in {self.run_dir}", self.out_log, self.global_log)
            return
        step_dir = Path(self.run_dir, steps[max(steps)])
        files = [path for path in step_dir.iterdir() if path.is_file() and path.name not in ("io.json", "params.cfg")
                 and any(path.match(pattern) for pattern in patterns)]
        if selected_models:
            with open(step_dir / "io.json") as json_file:
                models = jsonpickle.decode(json_file.read())["output"]
            for model in models:
                # Path of the model relative to the step folder, ie: ../04_flexref/flexref_1.pdb
                model_path = Path(str(model.rel_path))
                files.extend(Path(self.run_dir, model_path.parent.name).glob(model_path.name + "*"))
        if not files:
            fu.log("No output files found matching the criteria.", self.out_log, self.global_log)
        else:
            fu.zip_list(zip_path, files, self.out_log)

    def run_path(self, host_path: str) -> str:
        """Go from the host path of a file in the sandbox to the path haddock3 uses: it runs in the run folder."""
        return os.path.relpath(host_path, self.run_dir)

    def run(self) -> None:
        """Execute the HADDOCK step with common workflow."""
        input_wf_data = self.sandbox_file("input_haddock_wf_data")
        if input_wf_data[-4:] == ".zip":
            # Unzip workflow data to workflow_data_out
            new_input = fu.create_unique_dir(self.stage_io_dict["unique_dir"], '_input_unzipped')
            fu.unzip_list(input_wf_data, new_input)  # , self.out_log)
            input_wf_data = new_input

        # The run folder in the sandbox (host path): the output folder, or a folder zipped at the end
        wf_output = self.sandbox_file("output_haddock_wf_data")
        self.run_dir = self.create_tmp_dir() if wf_output[-4:] == ".zip" else wf_output
        if input_wf_data != self.run_dir:
            shutil.copytree(input_wf_data, self.run_dir, dirs_exist_ok=True)

        self.write_cfg()

        # haddock3 runs in the run folder, where the relative paths of the configuration are
        self.cmd = [self.binary_path, self.run_path(self.output_cfg_path)]

        if self.haddock_step_name != "haddock3_run":
            # By name: haddock3 looks for the run folder name in this path to compress the steps again
            self.cmd.extend(["--extend-run", f"../{Path(self.run_dir).name}"])
        elif getattr(self, "restart_from", None) is not None:
            restart_from = int(self.restart_from)
            if restart_from < 0:
                fu.log(f"Warning: restart_from must be a non-negative integer, {self.restart_from} given, "
                       "ignoring it.", self.out_log, self.global_log)
            else:
                fu.log(f"Restarting the run from step {restart_from}", self.out_log, self.global_log)
                self.cmd.extend(["--restart", str(restart_from)])

        # Run Biobb block
        self.run_biobb(cwd=self.run_dir)

        if self.step_zip:
            self.zip_step_files(self.step_zip, self.step_zip_files, self.zip_selected_models)
        if wf_output[-4:] == ".zip":
            zip_wf_output(self)

    def copy_to_host(self) -> None:
        """Copy the outputs to the host, first renaming in an existing output folder the step folders
        that haddock3 renumbered (0_topoaa to 00_topoaa): the copy only adds files."""
        output_wf = Path(self.io_dict["out"]["output_haddock_wf_data"])
        if output_wf.suffix != ".zip" and output_wf.is_dir() and output_wf.resolve() != Path(self.run_dir).resolve():
            for folder in ("", "data"):
                rename_step_folders(output_wf / folder, Path(self.run_dir) / folder, self.out_log, self.global_log)
        super().copy_to_host()


def create_cfg(
    output_cfg_path: str,
    workflow_dict: dict[str, Any],
    input_cfg_path: Optional[str] = None,
    properties_cfg_dict: Optional[dict[str, str]] = None,
    out_log: Optional[logging.Logger] = None,
    global_log: Optional[logging.Logger] = None,
) -> str:
    """Creates an CFG file using the following hierarchy: properties_cfg_dict > input_cfg_path > preset_dict"""
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
        if properties_cfg_dict:
            for k, v in properties_cfg_dict.items():
                fu.log(f"CFG from properties: {k} = {v}", out_log, global_log)
                cfg_dict[target_key][k] = v
    # Multiple steps: haddock3_run and haddock3_extend
    else:
        if properties_cfg_dict:
            for key, value in properties_cfg_dict.items():
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
        if haddock_step_name == "haddock3_run" and "run_dir" not in cfg_dict:
            cfg_dict["run_dir"] = "run"

    # Add molecules and run_dir if provided
    for key, value in workflow_dict.items():
        if key == 'haddock_step_name' or key in haddock_2_wf.values():
            continue
        fu.log(f"CFG: {key} = {value}", out_log, global_log)
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


def step_folders(folder: Path) -> dict[tuple[int, str], str]:
    """Go from a folder to its step folders (ie: 01_rigidbody) by step number and module name."""
    if not folder.is_dir():
        return {}
    steps = (re.fullmatch(r"(\d+)_(.+)", path.name) for path in folder.iterdir() if path.is_dir())
    return {(int(step[1]), step[2]): step[0] for step in steps if step}


def rename_step_folders(output_folder: Path, run_folder: Path, out_log: Optional[logging.Logger] = None,
                        global_log: Optional[logging.Logger] = None) -> None:
    """Give the step folders of **output_folder** the names they have in **run_folder**."""
    run_steps = step_folders(run_folder)
    for key, name in step_folders(output_folder).items():
        new_name = run_steps.get(key)
        if new_name and new_name != name and not (output_folder / new_name).exists():
            fu.log(f"Renaming {output_folder / name} to {new_name}, as haddock3 did", out_log, global_log)
            (output_folder / name).rename(output_folder / new_name)


def zip_wf_output(obj):
    """Zip the run folder into the workflow data output, in the sandbox."""
    dest_path = str(Path(obj.sandbox_file("output_haddock_wf_data")).with_suffix(''))
    fu.log(f"Zipping {obj.run_dir} to {dest_path} ", obj.out_log, obj.global_log)
    shutil.make_archive(dest_path, "zip", obj.run_dir)
