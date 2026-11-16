# type: ignore
from pathlib import Path

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

    def test_haddock3_restrain_bodies_stderr_not_in_output(self, noisy_properties, fake_warning):
        properties = {**self.properties, **noisy_properties('haddock3-restraints')}
        haddock3_restrain_bodies(properties=properties, **self.paths)
        assert fake_warning not in Path(self.paths['output_tbl_path']).read_text()
        assert fx.equal(self.paths['output_tbl_path'], self.paths['ref_output_tbl_path'])
        assert fake_warning in Path(properties['err_log_path']).read_text()
