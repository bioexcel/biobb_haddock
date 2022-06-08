from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.sele_top import sele_top


class TestSeleTop():
    def setUp(self):
        fx.test_setup(self, 'sele_top')

    def tearDown(self):
        pass
        #fx.test_teardown(self)

    def test_sele_top(self):
        sele_top(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_selection_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        assert fx.equal(self.paths['output_selection_zip_path'], self.paths['ref_output_selection_zip_path'])

