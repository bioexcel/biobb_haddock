# type: ignore
from pathlib import Path

from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig import haddock3_actpass_to_ambig


class TestHaddockActpassToAmbig():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_actpass_to_ambig')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock3_actpass_to_ambig(self):
        haddock3_actpass_to_ambig(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_tbl_path'])
        assert fx.equal(self.paths['output_tbl_path'], self.paths['ref_output_tbl_path'])

    def test_haddock3_actpass_to_ambig_stderr_not_in_output(self, noisy_properties, fake_warning):
        properties = {**self.properties, **noisy_properties('haddock3-restraints')}
        haddock3_actpass_to_ambig(properties=properties, **self.paths)
        assert fake_warning not in Path(self.paths['output_tbl_path']).read_text()
        assert fx.equal(self.paths['output_tbl_path'], self.paths['ref_output_tbl_path'])
        assert fake_warning in Path(properties['err_log_path']).read_text()
