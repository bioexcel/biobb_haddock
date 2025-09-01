# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.haddock3_extend import haddock3_extend


class TestHaddock3Extend():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_extend')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock3_extend(self):
        haddock3_extend(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_haddock_wf_data'])
        # assert fx.equal(self.paths['output_evaluation_zip_path'], self.paths['ref_output_evaluation_zip_path'])
