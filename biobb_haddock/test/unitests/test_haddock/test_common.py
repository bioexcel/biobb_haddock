# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_haddock.haddock.common import create_cfg
import toml


class TestCreateCfg():
    def setup_class(self):
        fx.test_setup(self, 'common')

    def teardown_class(self):
        pass
        # fx.test_teardown(self)

    def test_create_cfg_step(self):
        create_cfg(
            output_cfg_path=str(self.paths['output_cfg']),
            workflow_dict={'haddock_step_name': 'topoaa',
                           'run_dir': 'test_dir'},
            input_cfg_path=self.paths['input_cfg_step'],
            cfg_properties_dict=self.properties['cfg_step'],
        )

        assert fx.not_empty(self.paths['output_cfg'])
        with open(self.paths['output_cfg'], 'r') as f:
            cfg = toml.loads(f.read())

        assert cfg['run_dir'] == 'test_dir'             # From workflow_dict
        assert cfg['topoaa.1']['iniseed'] == 1          # From input_cfg
        assert cfg['topoaa.1']['tolerance'] == 5        # From cfg_properties_dict
        assert cfg['topoaa.1']["log_level"] == "quiet"  # From preset

    def test_create_cfg_run(self):
        create_cfg(
            output_cfg_path=str(self.paths['output_cfg']),
            workflow_dict={'haddock_step_name': 'haddock3_run', 'run_dir': 'test_dir',
                           'ambig_restraints_table_path': 'test_tbl'},
            input_cfg_path=self.paths['input_cfg_run'],
            cfg_properties_dict=self.properties['cfg_run'],
        )

        assert fx.not_empty(self.paths['output_cfg'])
        with open(self.paths['output_cfg'], 'r') as f:
            cfg = toml.loads(f.read())

        assert cfg['run_dir'] == 'test_dir'             # From workflow_dict
        assert cfg['topoaa.1']['iniseed'] == 1          # From input_cfg
        assert cfg['topoaa.1']['tolerance'] == 5        # From cfg_properties_dict
        assert cfg['rigidbody.1']['ambig_fname'] == 'test_tbl'
