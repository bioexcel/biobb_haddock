#!/usr/bin/env python3

"""Module containing the HADDOCK3 CapriEval class and the command line interface."""

from typing import Optional
import biobb_haddock.haddock.common as common


class CapriEval(common.HaddockStepBase):
    """
    | biobb_haddock CapriEval
    | Wrapper class for the HADDOCK3 CapriEval module.
    | The CapriEval module. `HADDOCK3 CapriEval module <https://www.bonvinlab.org/haddock3/modules/analysis/haddock.modules.analysis.caprieval.html>`_ computes Capri evaluation for a docking.

    Args:
        input_haddock_wf_data (dir): Path to the input directory containing all the current Haddock workflow data. File type: input. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip>`_. Accepted formats: directory (edam:format_1915).
        output_haddock_wf_data (dir): Path to the output directory containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_caprieval.zip>`_. Accepted formats: directory (edam:format_1915).
        output_evaluation_zip_path (str) (Optional): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_caprieval.zip>`_. Accepted formats: zip (edam:format_3987).
        reference_pdb_path (str) (Optional): Path to the input PDB file containing an structure for reference. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_1GGR.pdb>`_. Accepted formats: pdb (edam:format_1476).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
            * **global_cfg** (*dict*) - ({"postprocess": True}) `Global configuration options <https://www.bonvinlab.org/haddock3-user-manual/global_parameters.html>`_ specification.
            * **binary_path** (*str*) - ("haddock") Path to the haddock haddock executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - (None) Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.


    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_haddock.haddock.capri_eval import capri_eval
            prop = { 'binary_path': 'haddock' }
            capri_eval(input_haddock_wf_data='/path/to/myInputData',
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
        output_evaluation_zip_path: Optional[str] = None,
        reference_pdb_path: Optional[str] = None,
        haddock_config_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_haddock_wf_data": input_haddock_wf_data,
                "haddock_config_path": haddock_config_path,
                "reference_pdb_path": reference_pdb_path,
            },
            "out": {
                "output_haddock_wf_data": output_haddock_wf_data,
                "output_evaluation_zip_path": output_evaluation_zip_path,
            },
        }

        # Properties specific for HADDOCK Step
        self.haddock_step_name = "caprieval"
        # Handle configuration options from properties
        self.cfg = {k: str(v) for k, v in properties.get("cfg", dict()).items()}
        # Handle configuration options from arguments
        if reference_pdb_path:
            self.cfg["reference_fname"] = reference_pdb_path
        # Global HADDOCK configuration options
        self.global_cfg = properties.get("global_cfg", dict(postprocess=True))
        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")
        # Check the properties
        self.check_init(properties)

    def _handle_step_output(self):
        if output_evaluation_zip_path := self.io_dict["out"].get("output_evaluation_zip_path"):
            self.copy_step_output(
                lambda path: str(path).endswith(("izone", "aln", "tsv")),
                output_evaluation_zip_path
            )


def capri_eval(
    input_haddock_wf_data: str,
    output_haddock_wf_data: str,
    output_evaluation_zip_path: Optional[str] = None,
    reference_pdb_path: Optional[str] = None,
    haddock_config_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`CapriEval <biobb_haddock.haddock.capri_eval>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.capri_eval.launch>` method."""
    # Launch method inherited from HaddockStepBase
    return CapriEval(**dict(locals())).launch()


capri_eval.__doc__ = CapriEval.__doc__
main = CapriEval.get_main(capri_eval, 'Wrapper of the HADDOCK3 CapriEval module.')


if __name__ == "__main__":
    main()
