from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.haddock import haddock


class TesthaddockMipSingularity():
    def setUp(self):
        fx.test_setup(self, 'haddock_mip_singularity')

    def tearDown(self):
        #pass
        fx.test_teardown(self)

    def test_haddock_mip_singularity(self):
        haddock(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cube_path'])
        assert fx.not_empty(self.paths['output_grd_path'])
        assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
        assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])


class TesthaddockDockingSingularity():
    def setUp(self):
        fx.test_setup(self, 'haddock_docking_singularity')

    def tearDown(self):
        #pass
        fx.test_teardown(self)

    def test_haddock_docking_singularity(self):
        haddock(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.not_empty(self.paths['output_grd_path'])
        assert fx.not_empty(self.paths['output_rst_path'])
        # Can not compare PDB files formed excluvely by HETATM
        #assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_haddock_docking_pdb_path'])
        # GRD differs between executions
        #assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_docking_grd_path'])
        # RST differs between executions
        #assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_haddock_docking_rst_path'])

class TesthaddockEnergySingularity():
    def setUp(self):
        fx.test_setup(self, 'haddock_energy_singularity')

    def tearDown(self):
        #pass
        fx.test_teardown(self)

    def test_haddock_mip_singularity(self):
        haddock(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cube_path'])
        assert fx.not_empty(self.paths['output_grd_path'])
        assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
        assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])

class TesthaddockSolvationSingularity():
    def setUp(self):
        fx.test_setup(self, 'haddock_solvation_singularity')

    def tearDown(self):
        #pass
        fx.test_teardown(self)

    def test_haddock_mip_singularity(self):
        haddock(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cube_path'])
        assert fx.not_empty(self.paths['output_grd_path'])
        assert fx.equal(self.paths['output_grd_path'], self.paths['ref_output_haddock_mip_grd_path'])
        assert fx.equal(self.paths['output_cube_path'], self.paths['ref_output_haddock_mip_cube_path'])