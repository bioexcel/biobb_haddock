from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.haddock import haddock


# class TesthaddockMip():
#     def setUp(self):
#         fx.test_setup(self, 'haddock_mip')
#
#     def tearDown(self):
#         #pass
#         fx.test_teardown(self)
#
#     def test_haddock_mip(self):
#         haddock(properties=self.properties, **self.paths)
#         assert fx.not_empty(self.paths['output_cube_path'])
#         assert fx.not_empty(self.paths['output_grd_path'])
#         assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
#         assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])


# class TesthaddockDocking():
#     def setUp(self):
#         fx.test_setup(self, 'haddock_docking')
#
#     def tearDown(self):
#         #pass
#         fx.test_teardown(self)
#
#     def test_haddock_docking(self):
#         haddock(properties=self.properties, **self.paths)
#         assert fx.not_empty(self.paths['output_pdb_path'])
#         assert fx.not_empty(self.paths['output_grd_path'])
#         assert fx.not_empty(self.paths['output_rst_path'])
#         assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_haddock_docking_pdb_path'], remove_hetatm=False)
#         #assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_docking_grd_path'])
#         #assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_haddock_docking_rst_path'])


class TesthaddockEnergy():
    def setUp(self):
        fx.test_setup(self, 'haddock_energy')

    def tearDown(self):
        #pass
        fx.test_teardown(self)

    def test_haddock_energy(self):
        haddock(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_byat_path'])
        #assert fx.equal(self.paths['output_byat_path'], self.paths['ref_output_byat_path'])

# class TesthaddockSolvation():
#     def setUp(self):
#         fx.test_setup(self, 'haddock_solvation')
#
#     def tearDown(self):
#         #pass
#         fx.test_teardown(self)
#
#     def test_haddock_mip(self):
#         haddock(properties=self.properties, **self.paths)
#         assert fx.not_empty(self.paths['output_cube_path'])
#         assert fx.not_empty(self.paths['output_grd_path'])
#         assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
#         assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])