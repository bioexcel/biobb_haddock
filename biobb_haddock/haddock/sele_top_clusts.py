#!/usr/bin/env python3

"""Module containing the HADDOCK3 SeleTopClusts class and the command line interface."""

from typing import Optional
import biobb_haddock.haddock.common as common
from biobb_common.generic.biobb_object import launcher


class SeleTopClusts(common.HaddockStepBase):
    """
    | biobb_haddock SeleTopClusts
    | Wrapper class for the HADDOCK3 SeleTopClusts module.
    | The SeleTopClusts module. `HADDOCK3 SeleTopClusts module <https://www.bonvinlab.org/haddock3/modules/analysis/haddock.modules.analysis.seletopclusts.html>`_ selects the top clusters of a docking.

    Args:
        input_haddock_wf_data (dir): Path to the input directory containing all the current Haddock workflow data. File type: input. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_clustfcc.zip>`_. Accepted formats: directory (edam:format_1915), zip (edam:format_3987).
        output_haddock_wf_data (dir): Path to the output directory containing all the current Haddock workflow data. File type: output. Accepted formats: directory (edam:format_1915), zip (edam:format_3987).
        output_selection_zip_path (str) (Optional): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_seletop.zip>`_. Accepted formats: zip (edam:format_3987).
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

            from biobb_haddock.haddock.sele_top_clusts import sele_top_clusts
            prop = { 'binary_path': 'haddock' }
            sele_top_clusts(input_haddock_wf_data='/path/to/myInputData',
                           output_haddock_wf_data='/path/to/myOutputData',
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
        input_haddock_wf_data: str,
        output_haddock_wf_data: str,
        output_selection_zip_path: Optional[str] = None,
        haddock_config_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        super().__init__(**locals())

        # Properties specific for BB
        self.haddock_step_name = "seletopclusts"
        # Handle configuration options from propierties
        self.cfg = {k: v for k, v in self.cfg.items()}

    def _handle_step_output(self):
        """Zip the output files of the step, in the sandbox."""
        if output_selection_zip_path := self.sandbox_file("output_selection_zip_path"):
            self.copy_step_output(
                lambda path: str(path.name) not in ["io.json", "params.cfg"],
                output_selection_zip_path
            )


sele_top_clusts = launcher(SeleTopClusts)


if __name__ == "__main__":
    SeleTopClusts.main()
