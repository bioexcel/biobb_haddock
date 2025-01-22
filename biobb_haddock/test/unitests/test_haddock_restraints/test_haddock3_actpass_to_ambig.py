# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig import haddock3_actpass_to_ambig


class TestHaddockActpassToAmbig():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_actpass_to_ambig')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_capri_eval(self):
        haddock3_actpass_to_ambig(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_tbl_path'])
        # assert fx.equal(self.paths['output_tbl_path'], self.paths['ref_output_tbl_path'])
