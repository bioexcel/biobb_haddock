from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.capri_eval import capri_eval


class TestCapriEval():
    def setUp(self):
        fx.test_setup(self, 'capri_eval')

    def tearDown(self):
        pass
        #fx.test_teardown(self)

    def test_topology(self):
        capri_eval(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_evaluation_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        assert fx.equal(self.paths['output_evaluation_zip_path'], self.paths['ref_output_evaluation_zip_path'])

