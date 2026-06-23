# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.haddock3_run import haddock3_run
import os


class TestHaddock3Run():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_run')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock3_run(self):
        haddock3_run(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_haddock_wf_data'])
        assert len(os.listdir(self.paths['output_haddock_wf_data'])) > len(os.listdir(self.paths['input_haddock_wf_data'])), "The output directory should contain more files than the input directory"
        # assert fx.equal(self.paths['output_evaluation_zip_path'], self.paths['ref_output_evaluation_zip_path'])
