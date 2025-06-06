# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock3_restrain_bodies import haddock3_restrain_bodies


class TestHaddockRestrainBodies():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_restrain_bodies')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_capri_eval(self):
        haddock3_restrain_bodies(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_tbl_path'])
        assert fx.equal(self.paths['output_tbl_path'], self.paths['ref_output_tbl_path'])
