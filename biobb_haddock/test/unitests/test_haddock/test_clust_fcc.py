from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.clust_fcc import clust_fcc


class TestClustFCC():
    def setup_class(self):
        fx.test_setup(self, 'clust_fcc')

    def teardown_class(self):
        pass
        #fx.test_teardown(self)

    def test_clust_fcc(self):
        clust_fcc(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cluster_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        #assert fx.equal(self.paths['output_cluster_zip_path'], self.paths['ref_output_cluster_zip_path'])

