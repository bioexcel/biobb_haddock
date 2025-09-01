# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.haddock3_run import haddock3_run


class TestHaddock3Run():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_run')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock3_run(self):
        haddock3_run(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_haddock_wf_data'])
        # assert fx.equal(self.paths['output_evaluation_zip_path'], self.paths['ref_output_evaluation_zip_path'])
