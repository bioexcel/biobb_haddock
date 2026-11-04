# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.utils.biobb_anarcii import biobb_anarcii


class TestAnarcii():
    def setup_class(self):
        fx.test_setup(self, 'biobb_anarcii')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_biobb_anarcii(self):
        biobb_anarcii(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_pdb_path'])
