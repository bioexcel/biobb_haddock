from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.rigid_body import rigid_body


class TestRigidBody():
    def setUp(self):
        fx.test_setup(self, 'rigid_body')

    def tearDown(self):
        pass
        #fx.test_teardown(self)

    def test_rigid_body(self):
        rigid_body(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['docking_output_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        assert fx.equal(self.paths['docking_output_zip_path'], self.paths['ref_docking_output_zip_path'])

