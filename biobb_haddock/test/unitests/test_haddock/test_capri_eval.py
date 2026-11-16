# type: ignore
import re
from pathlib import Path

from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.capri_eval import capri_eval


class TestCapriEval():
    def setup_class(self):
        fx.test_setup(self, 'capri_eval')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_capri_eval(self):
        capri_eval(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_evaluation_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data'])
        # assert fx.equal(self.paths['output_evaluation_zip_path'], self.paths['ref_output_evaluation_zip_path'])

        # reference_pdb_path must reach haddock3 as reference_fname: without it,
        # caprieval scores every model against the best-scoring model instead
        params = sorted(Path(self.paths['output_haddock_wf_data']).glob('*_caprieval/params.cfg'))
        assert params, 'no caprieval params.cfg in the output run directory'
        reference = re.search(r'^reference_fname\s*=\s*"(.*)"', params[-1].read_text(), re.MULTILINE)
        assert reference, 'reference_fname missing from the caprieval params.cfg'
        assert Path(reference.group(1)).name == Path(self.paths['reference_pdb_path']).name
