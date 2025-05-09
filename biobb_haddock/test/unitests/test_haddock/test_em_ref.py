# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.em_ref import em_ref
import warnings


class TestEMRef():
    def setup_class(self):
        fx.test_setup(self, 'em_ref')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_em_ref(self):
        em_ref(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['refinement_output_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        # assert fx.equal(self.paths['refinement_output_zip_path'], self.paths['ref_refinement_output_zip_path'])
        warnings.warn(
            "The content of the output_haddock_wf_data_zip is not being checked.\n"
            f"Do it manually at {self.testfile_dir}")
