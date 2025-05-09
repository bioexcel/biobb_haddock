# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.capri_eval import capri_eval
import warnings


class TestCapriEval():
    def setup_class(self):
        fx.test_setup(self, 'capri_eval')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_capri_eval(self):
        capri_eval(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_evaluation_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        # assert fx.equal(self.paths['output_evaluation_zip_path'], self.paths['ref_output_evaluation_zip_path'])
        warnings.warn(
            "The content of the output_haddock_wf_data_zip is not being checked.\n"
            f"Do it manually at {self.testfile_dir}")
