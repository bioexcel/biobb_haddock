# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.sele_top_clusts import sele_top_clusts


class TestSeleTopClusts():
    def setup_class(self):
        fx.test_setup(self, 'sele_top_clusts')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_sele_top_clusts(self):
        sele_top_clusts(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_selection_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data'])
        # assert fx.equal(self.paths['output_selection_zip_path'], self.paths['ref_output_selection_zip_path'])
