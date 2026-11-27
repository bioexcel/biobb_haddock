# type: ignore
import sys
import zipfile

import pytest

from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.topology import topology


class TestTopologyDocker():
    def setup_class(self):
        fx.test_setup(self, 'topology_docker')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_topology_docker(self):
        topology(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['mol1_output_top_zip_path'])
        assert fx.not_empty(self.paths['mol2_output_top_zip_path'])
        assert zipfile.is_zipfile(self.paths['output_haddock_wf_data'])


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestTopologySingularity():
    def setup_class(self):
        fx.test_setup(self, 'topology_singularity')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_topology_singularity(self):
        topology(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['mol1_output_top_zip_path'])
        assert fx.not_empty(self.paths['mol2_output_top_zip_path'])
        assert zipfile.is_zipfile(self.paths['output_haddock_wf_data'])
