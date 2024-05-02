from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.flex_ref import flex_ref


class TestFlexRef():
    def setup_class(self):
        fx.test_setup(self, 'flex_ref')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_flex_ref(self):
        flex_ref(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['refinement_output_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data_zip'])
        assert fx.equal(self.paths['refinement_output_zip_path'], self.paths['ref_refinement_output_zip_path'])
