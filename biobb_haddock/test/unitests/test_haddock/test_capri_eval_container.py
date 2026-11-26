# type: ignore
import sys

import pytest

from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.capri_eval import capri_eval


class TestCapriEvalDocker():
    def setup_class(self):
        fx.test_setup(self, 'capri_eval_docker')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_capri_eval_docker(self):
        capri_eval(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_evaluation_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data'])


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestCapriEvalSingularity():
    def setup_class(self):
        fx.test_setup(self, 'capri_eval_singularity')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_capri_eval_singularity(self):
        capri_eval(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_evaluation_zip_path'])
        assert fx.not_empty(self.paths['output_haddock_wf_data'])
