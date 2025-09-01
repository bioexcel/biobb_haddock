#!/usr/bin/env python3

"""Module containing the HADDOCK3 FlexRef class and the command line interface."""

from typing import Optional
import biobb_haddock.haddock.common as common


class FlexRef(common.HaddockStepBase):
    """
    | biobb_haddock FlexRef
    | Wrapper class for the HADDOCK3 FlexRef module.
    | The FlexRef module.`HADDOCK3 FlexRef module <https://www.bonvinlab.org/haddock3/modules/refinement/haddock.modules.refinement.flexref.html>`_ computes a flexible refinement over selected structures.

    Args:
        input_haddock_wf_data (dir): Path to the input directory containing all the current Haddock workflow data. File type: input. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip>`_. Accepted formats: directory (edam:format_1915).
        output_haddock_wf_data (dir): Path to the output directory containing all the current Haddock workflow data. File type: output. `Sample file <https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip>`_. Accepted formats: directory (edam:format_1915).
        refinement_output_zip_path (str) (Optional): Path to the output PDB file collection in zip format. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip>`_. Accepted formats: zip (edam:format_3987).
        ambig_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        unambig_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
        hb_restraints_table_path (str) (Optional): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl>`_. Accepted formats: tbl (edam:format_2330).
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

            from biobb_haddock.haddock.flex_ref import flex_ref
            prop = { 'binary_path': 'haddock' }
            flex_ref(input_haddock_wf_data='/path/to/myInputData',
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
        refinement_output_zip_path: Optional[str] = None,
        ambig_restraints_table_path: Optional[str] = None,
        unambig_restraints_table_path: Optional[str] = None,
        hb_restraints_table_path: Optional[str] = None,
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
                "ambig_restraints_table_path": ambig_restraints_table_path,
                "unambig_restraints_table_path": unambig_restraints_table_path,
                "hb_restraints_table_path": hb_restraints_table_path,
                "haddock_config_path": haddock_config_path,
            },
            "out": {
                "output_haddock_wf_data": output_haddock_wf_data,
                "refinement_output_zip_path": refinement_output_zip_path,
            },
        }

        # Properties specific for BB
        self.haddock_step_name = "flexref"
        # Handle configuration options from propierties
        self.cfg = {k: str(v) for k, v in properties.get("cfg", dict()).items()}
        # Handle configuration options from arguments
        if ambig_restraints_table_path:
            self.cfg["ambig_fname"] = ambig_restraints_table_path
        if unambig_restraints_table_path:
            self.cfg["unambig_fname"] = unambig_restraints_table_path
        if hb_restraints_table_path:
            self.cfg["hbond_fname"] = hb_restraints_table_path
        # Global HADDOCK configuration options
        self.global_cfg = properties.get("global_cfg", dict(postprocess=False))
        # Properties specific for BB
        self.binary_path = properties.get("binary_path", "haddock3")
        # Check the properties
        self.check_init(properties)

    def _handle_step_output(self):
        if refinement_output_zip_path := self.io_dict["out"].get("refinement_output_zip_path"):
            self.copy_step_output(
                lambda path: path.match(self.haddock_step_name + r"*.pdb*"),
                refinement_output_zip_path
            )


def flex_ref(
    input_haddock_wf_data: str,
    output_haddock_wf_data: str,
    refinement_output_zip_path: Optional[str] = None,
    ambig_restraints_table_path: Optional[str] = None,
    unambig_restraints_table_path: Optional[str] = None,
    hb_restraints_table_path: Optional[str] = None,
    haddock_config_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`FlexRef <biobb_haddock.haddock.flex_ref>` class and
    execute the :meth:`launch() <biobb_haddock.haddock.flex_ref.launch>` method."""
    # Launch method inherited from HaddockStepBase
    return FlexRef(**dict(locals())).launch()


flex_ref.__doc__ = FlexRef.__doc__
main = FlexRef.get_main(flex_ref, "Wrapper of the HADDOCK3 FlexRef module.")


if __name__ == "__main__":
    main()
