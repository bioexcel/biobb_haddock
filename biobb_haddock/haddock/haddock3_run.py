#!/usr/bin/env python3

"""Module containing the HADDOCK3 Run class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_haddock.haddock.common import create_cfg, move_to_container_path, zip_wf_output


class Haddock3Run(BiobbObject):
    """
    | biobb_haddock Haddock3Run
    | Wrapper class for the HADDOCK3 Run module.
    | The HADDOCK3 run module launches the HADDOCK3 execution for docking.

    Args:
        input_folder (dir): Input folder containing all the files defined in the config. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G.pdb>`_. Accepted formats: directory (edam:format_1915), zip (edam:format_3987).
        output_haddock_wf_data (dir): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip>`_. Accepted formats: (edam:format_1915), zip (edam:format_3987).
        haddock_config_path (str) (Optional): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        properties (dict - Python dictionary object containing the tool parameters, not input/output files):
            * **cfg** (*dict*) - ({}) Haddock configuration options specification.
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

            from biobb_haddock.haddock.haddock3_run import haddock3_run
            haddock3_run(input_folder='/path/to/input_folder.pdb',
                         output_haddock_wf_data='/path/to/haddock_output.zip',
                         haddock_config_path='/path/to/myHaddockConfig.cfg',
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
        input_folder: str,
        output_haddock_wf_data: str,
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
                "input_folder": input_folder,
                "haddock_config_path": haddock_config_path,
            },
            "out": {
                "output_haddock_wf_data": output_haddock_wf_data,
            },
        }

        # Properties specific for BB
        self.output_cfg_path = properties.get("output_cfg_path", "haddock.cfg")
        self.cfg = {k: str(v)
                    for k, v in properties.get("cfg", dict()).items()}

        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")

        # Check the properties
        self.check_init(properties)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Haddock3Run <biobb_haddock.haddock.haddock3_run>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        workflow_dict = {"run_dir": self.stage_io_dict["out"]["output_haddock_wf_data"]}

        # Create data dir
        output_cfg_path = create_cfg(
            output_cfg_path=self.create_tmp_file('_haddock.cfg'),
            workflow_dict=workflow_dict,
            input_cfg_path=self.stage_io_dict["in"].get("haddock_config_path"),
            cfg_properties_dict=self.cfg,
            out_log=self.out_log,
            global_log=self.global_log
        )

        if self.container_path:
            fu.log("Container execution enabled", self.out_log)
            move_to_container_path(self)

        with fu.change_dir(self.stage_io_dict["unique_dir"]):
            self.cmd = [self.binary_path, output_cfg_path]
            # Run Biobb block
            self.run_biobb()

        # Copy files to host
        if self.io_dict["out"]["output_haddock_wf_data"][-4:] == ".zip":
            zip_wf_output(self, str(workflow_dict["run_dir"]))
        else:
            self.copy_to_host()

        # Remove temporal files
        self.remove_tmp_files()

        return self.return_code


def haddock3_run(
        input_folder: str,
        output_haddock_wf_data: str,
        haddock_config_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
) -> int:
    """Create :class:`Haddock3Run <biobb_haddock.haddock.haddock3_run>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.haddock3_run.launch>` method."""
    return Haddock3Run(**dict(locals())).launch()


haddock3_run.__doc__ = Haddock3Run.__doc__
main = Haddock3Run.get_main(haddock3_run, "Wrapper of the HADDOCK3 Haddock3Run module.")


if __name__ == "__main__":
    main()
