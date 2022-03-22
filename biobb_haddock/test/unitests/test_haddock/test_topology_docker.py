from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.haddock import haddock


# class TesthaddockMipDocker():
#     def setUp(self):
#         fx.test_setup(self, 'haddock_mip_docker')
#
#     def tearDown(self):
#         #pass
#         fx.test_teardown(self)
#
#     def test_haddock_mip_docker(self):
#         haddock(properties=self.properties, **self.paths)
#         assert fx.not_empty(self.paths['output_cube_path'])
#         assert fx.not_empty(self.paths['output_grd_path'])
#         assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
#         assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])


# class TesthaddockDockingDocker():
#     def setUp(self):
#         fx.test_setup(self, 'haddock_docking_docker')
#
#     def tearDown(self):
#         pass
#         #fx.test_teardown(self)
#
#     def test_haddock_docking_docker(self):
#         haddock(properties=self.properties, **self.paths)
#         assert fx.not_empty(self.paths['output_pdb_path'])
#         assert fx.not_empty(self.paths['output_grd_path'])
#         assert fx.not_empty(self.paths['output_rst_path'])
#         # Can not compare PDB files formed excluvely by HETATM
#         #assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_haddock_docking_pdb_path'])
#         # GRD differs between executions
#         #assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_docking_grd_path'])
#         # RST differs between executions
#         #assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_haddock_docking_rst_path'])

class TesthaddockEnergyDocker():
    def setUp(self):
        fx.test_setup(self, 'haddock_energy_docker')

    def tearDown(self):
        # pass
        fx.test_teardown(self)

    def test_haddock_energy(self):
        haddock(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_byat_path'])
        # assert fx.equal(self.paths['output_byat_path'], self.paths['ref_output_byat_path'])

# class TesthaddockSolvationDocker():
#     def setUp(self):
#         fx.test_setup(self, 'haddock_solvation_docker')
#
#     def tearDown(self):
#         #pass
#         fx.test_teardown(self)
#
#     def test_haddock_mip_docker(self):
#         haddock(properties=self.properties, **self.paths)
#         assert fx.not_empty(self.paths['output_cube_path'])
#         assert fx.not_empty(self.paths['output_grd_path'])
#         assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
#         assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])