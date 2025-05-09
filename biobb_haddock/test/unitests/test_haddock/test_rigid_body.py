# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.rigid_body import rigid_body
import warnings


class TestRigidBody():
    def setup_class(self):
        fx.test_setup(self, 'rigid_body')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_rigid_body(self):
        rigid_body(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['docking_output_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        # assert fx.equal(self.paths['docking_output_zip_path'], self.paths['ref_docking_output_zip_path'])
        warnings.warn(
            "The content of the output_haddock_wf_data_zip is not being checked.\n"
            f"Do it manually at {self.testfile_dir}")
