#!/usr/bin/env python3

"""Module containing the HADDOCK3 Run class and the command line interface."""

from typing import Optional
import biobb_haddock.haddock.common as common


class Haddock3Run(common.HaddockStepBase):
    """
    | biobb_haddock Haddock3Run
    | Wrapper class for the HADDOCK3 Run module.
    | The HADDOCK3 run module launches the HADDOCK3 execution for docking.

    Args:
        input_haddock_wf_data (dir): Input folder containing all the files defined in the config. File type: input. `Sample folder <https://github.com/bioexcel/biobb_haddock/tree/master/biobb_haddock/test/data/haddock/haddock_wf_data_run.zip>`_. Accepted formats: directory (edam:format_1915), zip (edam:format_3987).
        output_haddock_wf_data (dir): Path to the output zipball containing all the current Haddock workflow data. File type: output. Accepted formats: directory (edam:format_1915), zip (edam:format_3987).
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
            haddock3_run(input_haddock_wf_data='/path/to/myInputData',
                         output_haddock_wf_data='/path/to/myOutputData',
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
        input_haddock_wf_data: str,
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
                "input_haddock_wf_data": input_haddock_wf_data,
                "haddock_config_path": haddock_config_path,
            },
            "out": {
                "output_haddock_wf_data": output_haddock_wf_data,
            },
        }

        # Properties specific for HADDOCK Step
        self.haddock_step_name = "haddock3_run"
        # Handle configuration options from properties
        self.cfg = {k: v for k, v in properties.get("cfg", dict()).items()}
        # Global HADDOCK configuration options
        self.global_cfg = properties.get("global_cfg", dict(postprocess=True))
        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")
        # Check the properties
        self.check_init(properties)


def haddock3_run(
        input_haddock_wf_data: str,
        output_haddock_wf_data: str,
        haddock_config_path: Optional[str] = None,
        properties: Optional[dict] = None,
        **kwargs,
) -> int:
    """Create :class:`Haddock3Run <biobb_haddock.haddock.haddock3_run>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.haddock3_run.launch>` method."""
    # Launch method inherited from HaddockStepBase
    return Haddock3Run(**dict(locals())).launch()


haddock3_run.__doc__ = Haddock3Run.__doc__
main = Haddock3Run.get_main(haddock3_run, "Wrapper of the HADDOCK3 Haddock3Run module.")


if __name__ == "__main__":
    main()
