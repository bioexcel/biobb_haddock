# type: ignore
from pathlib import Path

from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock_restraints.haddock3_accessibility import haddock3_accessibility


class TestHaddockAccessibility():
    def setup_class(self):
        fx.test_setup(self, 'haddock3_accessibility')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_haddock3_accessibility(self):
        haddock3_accessibility(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_accessibility_path'])
        assert fx.not_empty(self.paths['output_actpass_path'])
        # equal is comparing log timestamps
        # assert fx.equal(self.paths['output_accessibility_path'], self.paths['ref_output_accessibility_path'])
        assert fx.equal(self.paths['output_actpass_path'], self.paths['ref_output_actpass_path'])

    def test_haddock3_accessibility_stderr_not_in_output(self, noisy_properties, fake_warning):
        properties = {**self.properties, **noisy_properties('haddock3-restraints')}
        # The tool does not overwrite an existing actpass file, so remove the one left by the previous test
        Path(f"{Path(self.paths['input_pdb_path']).stem}_passive_A.actpass").unlink(missing_ok=True)
        haddock3_accessibility(properties=properties, **self.paths)
        # The report is the tool's stderr: only its log records must be kept
        report = Path(self.paths['output_accessibility_path']).read_text()
        assert fake_warning not in report
        assert 'warnings.warn(' not in report
        assert 'Chain A - ' in report
        assert fx.equal(self.paths['output_actpass_path'], self.paths['ref_output_actpass_path'])
        assert fake_warning in Path(properties['err_log_path']).read_text()
