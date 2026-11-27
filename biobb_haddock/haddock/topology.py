#!/usr/bin/env python3

"""Module containing the HADDOCK3 Topology class and the command line interface."""

from pathlib import Path
from typing import Optional
import biobb_haddock.haddock.common as common
from biobb_common.generic.biobb_object import launcher


class Topology(common.HaddockStepBase):
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

    haddock_step_name = "topoaa"

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

    def run(self) -> None:
        """Start a HADDOCK3 run with the topologies of the molecules: haddock3 creates the run folder, named
        after the output (without .zip), in the sandbox where it runs."""
        # The run folder relative to the sandbox, and its host path for the Python code
        run_dir = self.stage_io_dict["out"]["output_haddock_wf_data"]
        run_dir = run_dir[:-4] if run_dir[-4:] == ".zip" else run_dir
        self.run_dir = str(Path(self.stage_io_dict["unique_dir"], run_dir))
        molecules = [self.stage_io_dict["in"][mol] for mol in ("mol1_input_pdb_path", "mol2_input_pdb_path")
                     if self.io_dict["in"].get(mol)]
        self.write_cfg(run_dir=run_dir, molecules=molecules)

        self.cmd = [self.binary_path, self.staged_path(self.output_cfg_path)]
        self.run_biobb()

        for mol in ("mol1", "mol2"):
            if input_pdb := self.io_dict["in"].get(f"{mol}_input_pdb_path"):
                self.zip_step_files(f"{mol}_output_top_zip_path", [f"{Path(input_pdb).stem}*_haddock.pdb*"])
        if self.stage_io_dict["out"]["output_haddock_wf_data"][-4:] == ".zip":
            common.zip_wf_output(self)


topology = launcher(Topology)


if __name__ == "__main__":
    Topology.main()
