#!/usr/bin/env python3

"""Module containing the HADDOCK3 SeleTop class and the command line interface."""


from pathlib import Path
from typing import Optional

from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
import biobb_haddock.haddock.common as common


class SeleTop(BiobbObject):
    """
    | biobb_haddock SeleTop
    | Wrapper class for the HADDOCK3 SeleTop module.
    | The SeleTop module. `HADDOCK3 SeleTop module <https://www.bonvinlab.org/haddock3/modules/analysis/haddock.modules.analysis.seletop.html>`_ selects the top models of a docking.

    Args:
        input_haddock_wf_data_zip (str): Path to the input zipball containing all the current Haddock workflow data. File type: input. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip>`_. Accepted formats: zip (edam:format_3987).
        output_selection_zip_path (str): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_seletop.zip>`_. Accepted formats: zip (edam:format_3987).
        output_haddock_wf_data_zip (str) (Optional): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip>`_. Accepted formats: zip (edam:format_3987).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
            * **global_cfg** (*dict*) - ({"postprocess": False}) `Global configuration options <https://www.bonvinlab.org/haddock3-user-manual/global_parameters.html>`_ specification.
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

            from biobb_haddock.haddock.sele_top import sele_top
            prop = { 'binary_path': 'haddock' }
            sele_top(input_haddock_wf_data_zip='/path/to/myworkflowdata.zip',
                       output_evaluation_zip='/path/to/myevalfiles.zip',
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
        input_haddock_wf_data_zip: str,
        output_selection_zip_path: str,
        output_haddock_wf_data_zip: Optional[str] = None,
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
            "in": {"haddock_config_path": haddock_config_path},
            "out": {
                "output_haddock_wf_data_zip": output_haddock_wf_data_zip,
                "output_selection_zip_path": output_selection_zip_path,
            },
        }
        # Should not be copied inside container
        self.input_haddock_wf_data_zip = input_haddock_wf_data_zip

        # Properties specific for BB
        self.haddock_step_name = "seletop"
        self.output_cfg_path = properties.get("output_cfg_path", "haddock.cfg")
        self.cfg = {k: v for k, v in properties.get("cfg", dict()).items()}
        self.global_cfg = properties.get("global_cfg", dict(postprocess=False))

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")

        # Check the properties
        self.check_init(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`SeleTop <biobb_haddock.haddock.sele_top>` object."""
        # tmp_files = []

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Unzip workflow data to workflow_data_out
        run_dir = common.unzip_workflow_data(
            zip_file=self.input_haddock_wf_data_zip, out_log=self.out_log
        )

        workflow_dict = {"haddock_step_name": self.haddock_step_name}
        workflow_dict.update(self.global_cfg)

        # Create data dir
        cfg_dir = fu.create_unique_dir()
        self.output_cfg_path = common.create_cfg(
            output_cfg_path=str(Path(cfg_dir).joinpath(self.output_cfg_path)),
            workflow_dict=workflow_dict,
            input_cfg_path=self.stage_io_dict["in"].get("haddock_config_path"),
            cfg_properties_dict=self.cfg,
        )

        if self.container_path:
            fu.log("Container execution enabled", self.out_log)
            common.move_to_container_path(self, run_dir)

        self.cmd = [self.binary_path, self.output_cfg_path, "--extend-run", run_dir]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        common.copy_step_output(
            self, run_dir,
            lambda path: str(path.name) not in ["io.json", "params.cfg"],
            self.io_dict["out"]["output_selection_zip_path"],
            sele_top=True
        )

        # Create zip output
        if self.io_dict["out"].get("output_haddock_wf_data_zip"):
            common.zip_wf_output(self, run_dir)

        # Remove temporal files
        self.tmp_files.extend([run_dir, cfg_dir])
        self.remove_tmp_files()

        return self.return_code


def sele_top(
    input_haddock_wf_data_zip: str,
    output_selection_zip_path: str,
    output_haddock_wf_data_zip: Optional[str] = None,
    haddock_config_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`SeleTop <biobb_haddock.haddock.sele_top>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.sele_top.launch>` method."""
    return SeleTop(**dict(locals())).launch()


sele_top.__doc__ = SeleTop.__doc__
main = SeleTop.get_main(sele_top, "Wrapper of the HADDOCK3 SeleTop module.")


if __name__ == "__main__":
    main()
