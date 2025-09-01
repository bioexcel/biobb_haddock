#!/usr/bin/env python3

"""Module containing the haddock3 run class and the command line interface."""

from typing import Optional
import biobb_haddock.haddock.common as common


class Haddock3Extend(common.HaddockStepBase):
    """
    | biobb_haddock Haddock3Extend
    | Wrapper class for the HADDOCK3 extend module.
    | The `HADDOCK3 extend <https://www.bonvinlab.org/haddock3/tutorials/continuing_runs.html>`_. module continues the HADDOCK3 execution for docking of an already started run.

    Args:
        input_haddock_wf_data (dir): Path to the input zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip>`_. Accepted formats: zip (edam:format_3987).
        haddock_config_path (str): Haddock configuration CFG file path. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg>`_. Accepted formats: cfg (edam:format_1476).
        output_haddock_wf_data (dir): Path to the output zipball containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip>`_. Accepted formats: zip (edam:format_3987).
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

            from biobb_haddock.haddock.haddock3_extend import haddock3_extend
            haddock3_extend(input_haddock_wf_data='/path/to/myworkflowdata.zip',
                            haddock_config_path='/path/to/myHaddockConfig.cfg',
                            output_haddock_wf_data='/path/to/haddock_output.zip',
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
        haddock_config_path: str,
        output_haddock_wf_data: str,
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

        # Properties specific for BB
        self.haddock_step_name = "haddock3_extend"
        # Handle configuration options from properties
        self.cfg = {k: str(v) for k, v in properties.get("cfg", dict()).items()}
        # Global HADDOCK configuration options
        self.global_cfg = properties.get("global_cfg", dict(postprocess=True))
        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")
        # Check the properties
        self.check_init(properties)


def haddock3_extend(
    input_haddock_wf_data: str,
    haddock_config_path: str,
    output_haddock_wf_data: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Haddock3Extend <biobb_haddock.haddock.haddock3_extend>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.haddock3_extend.launch>` method."""
    return Haddock3Extend(**dict(locals())).launch()


haddock3_extend.__doc__ = Haddock3Extend.__doc__
main = Haddock3Extend.get_main(haddock3_extend, "Wrapper of the HADDOCK3 Haddock3Extend module.")


if __name__ == "__main__":
    main()
