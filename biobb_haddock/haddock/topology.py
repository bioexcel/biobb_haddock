#!/usr/bin/env python3

"""Module containing the HADDOCK3 Topology class and the command line interface."""

from pathlib import Path
from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu
from biobb_haddock.haddock.common import create_cfg, zip_wf_output


class Topology(BiobbObject):
    """
    | biobb_haddock Topology
    | Wrapper class for the HADDOCK3 Topology module.
    | The Topology module. `HADDOCK3 Topology module <https://www.bonvinlab.org/haddock3/modules/topology/haddock.modules.topology.topoaa.html#haddock.modules.topology.topoaa.HaddockModule>`_ creates a topology from a system to be used for docking.

    Args:
        mol1_input_pdb_path (str): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G.pdb>`_. Accepted formats: pdb (edam:format_1476).
        mol1_output_top_zip_path (str) (Optional): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_mol1_top.zip>`_. Accepted formats: zip (edam:format_3987).
        mol2_input_pdb_path (str) (Optional): Path to the input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/hpr_ensemble.pdb>`_. Accepted formats: pdb (edam:format_1476).
        mol2_output_top_zip_path (str) (Optional): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_mol2_top.zip>`_. Accepted formats: zip (edam:format_3987).
        output_haddock_wf_data (dir): Path to the output directory containing all the current Haddock workflow data. File type: output. Accepted formats: directory (edam:format_1915), zip (edam:format_3987).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
            * **global_cfg** (*dict*) - ({"postprocess": False}) `Global configuration options <https://www.bonvinlab.org/haddock3-user-manual/global_parameters.html>`_ specification.
            * **binary_path** (*str*) - ("haddock3") Path to the haddock haddock executable binary.
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

            from biobb_haddock.haddock.topology import topology
            prop = { 'binary_path': 'haddock' }
            topology(mol1_input_pdb_path='/path/to/myStructure.pdb',
                     mol1_output_top_zip_path='/path/to/topology.zip',
                     properties=prop)

    Info:
        * wrapped_software:
            * name: HADDOCK3
            * version: 2025.5
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(
        self,
        mol1_input_pdb_path: str,
        output_haddock_wf_data: str,
        mol1_output_top_zip_path: Optional[str] = None,
        mol2_input_pdb_path: Optional[str] = None,
        mol2_output_top_zip_path: Optional[str] = None,
        haddock_config_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        super().__init__(**locals())

        # Properties specific for BB
        self.haddock_step_name = "topoaa"
        # Handle configuration options from propierties
        self.cfg = {k: v for k, v in self.cfg.items()}

    def run(self) -> None:
        """Execute the :class:`Topology <biobb_haddock.haddock.topology>` object."""

        # The run directory, named after the output (without .zip): relative to the sandbox, where haddock3 runs
        run_dir = self.stage_io_dict["out"]["output_haddock_wf_data"]
        run_dir = run_dir[:-4] if run_dir[-4:] == ".zip" else run_dir
        # Its host path, for the Python code
        self.run_dir = str(Path(self.stage_io_dict["unique_dir"], run_dir))
        workflow_dict = {
            "run_dir": run_dir,
            "molecules": [self.stage_io_dict["in"]["mol1_input_pdb_path"]],
            "haddock_step_name": self.haddock_step_name,
        }
        workflow_dict.update(self.global_cfg)

        if mol2_input_pdb_path := self.stage_io_dict["in"].get("mol2_input_pdb_path"):
            workflow_dict["molecules"].append(mol2_input_pdb_path)

        # Create workflow configuration
        self.output_cfg_path = create_cfg(
            output_cfg_path=self.create_tmp_file('_haddock.cfg'),
            workflow_dict=workflow_dict,
            input_cfg_path=self.sandbox_file("haddock_config_path"),
            properties_cfg_dict=self.cfg,
        )

        self.cmd = [self.binary_path, self.staged_path(self.output_cfg_path)]

        # Run Biobb block
        self.run_biobb()

        # Copy output
        haddock_output_path = Path(f'{self.run_dir}/0_{self.haddock_step_name}')
        mol1_name = str(Path(self.io_dict["in"]["mol1_input_pdb_path"]).stem)
        mol1_output_file_list = list(
            haddock_output_path.glob(mol1_name + r"*_haddock.pdb*")
        )
        fu.zip_list(
            self.sandbox_file("mol1_output_top_zip_path"),
            mol1_output_file_list,
        )

        if self.io_dict["out"].get("mol2_output_top_zip_path"):
            mol2_name = str(Path(self.io_dict["in"]["mol2_input_pdb_path"]).stem)
            mol2_output_file_list = list(
                haddock_output_path.glob(mol2_name + r"*_haddock.pdb*")
            )
            fu.zip_list(
                self.sandbox_file("mol2_output_top_zip_path"),
                mol2_output_file_list,
                self.out_log,
            )

        # Create zip output
        if self.stage_io_dict["out"]["output_haddock_wf_data"][-4:] == ".zip":
            zip_wf_output(self)


topology = launcher(Topology)


if __name__ == "__main__":
    Topology.main()
