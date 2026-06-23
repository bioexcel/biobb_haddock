# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock_interface import haddock_interface


class TestHaddockInterface():
    def setup_class(self):
        fx.test_setup(self, 'haddock_interface')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock_interface(self):
        haddock_interface(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_txt_path'])
        assert fx.equal(self.paths['output_txt_path'], self.paths['ref_output_txt_path'])
