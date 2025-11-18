# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock3_accessibility import haddock3_accessibility


class TestHaddockAccessibility():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_accessibility')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_capri_eval(self):
        haddock3_accessibility(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_accessibility_path'])
        assert fx.not_empty(self.paths['output_actpass_path'])
        # equal is comparing log timestamps
        # assert fx.equal(self.paths['output_accessibility_path'], self.paths['ref_output_accessibility_path'])
        assert fx.equal(self.paths['output_actpass_path'], self.paths['ref_output_actpass_path'])
