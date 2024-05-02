from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.topology import topology


class TestTopology():
    def setup_class(self):
        fx.test_setup(self, 'topology')

    def teardown_class(self):
        # pass
        fx.test_teardown(self)

    def test_topology(self):
        topology(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['mol1_output_top_zip_path'])
        assert fx.not_empty(self.paths['mol2_output_top_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        # assert fx.equal(self.paths['mol1_output_top_zip_path'], self.paths['ref_mol1_output_top_zip_path'])
        # assert fx.equal(self.paths['mol2_output_top_zip_path'], self.paths['ref_mol2_output_top_zip_path'])
