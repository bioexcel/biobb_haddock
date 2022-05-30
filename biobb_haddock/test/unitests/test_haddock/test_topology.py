from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.topology import topology


class TestTopology():
    def setUp(self):
        fx.test_setup(self, 'topology')

    def tearDown(self):
        pass
        #fx.test_teardown(self)

    def test_topology(self):
        topology(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_top_zip'])
        assert fx.equal(self.paths['output_top_zip'], self.paths['ref_output_top_zip'])
