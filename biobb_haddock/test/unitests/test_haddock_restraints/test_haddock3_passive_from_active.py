# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock3_passive_from_active import haddock3_passive_from_active


class TestHaddockPassiveFromActive():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_passive_from_active')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock3_passive_from_active(self):
        haddock3_passive_from_active(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_actpass_path'])
        assert fx.equal(self.paths['output_actpass_path'], self.paths['ref_output_actpass_path'])
