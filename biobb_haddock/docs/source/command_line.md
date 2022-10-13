# BioBB HADDOCK Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Em_ref
Wrapper class for the Haddock EMRef module.
### Get help
Command:
```python
em_ref -h
```
    /bin/sh: em_ref: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **refinement_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **** (*string*): Path to the input TBL file containing a list of restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_em_ref.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
em_ref --config config_em_ref.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip -- e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_em_ref.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
em_ref --config config_em_ref.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip -- e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Sele_top
Wrapper class for the Haddock SeleTop module.
### Get help
Command:
```python
sele_top -h
```
    /bin/sh: sele_top: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip). Accepted formats: ZIP
* **output_selection_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_seletop.zip). Accepted formats: ZIP
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_sele_top.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
sele_top --config config_sele_top.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_sele_top.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
sele_top --config config_sele_top.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Capri_eval
Wrapper class for the Haddock CapriEval module.
### Get help
Command:
```python
capri_eval -h
```
    /bin/sh: capri_eval: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip). Accepted formats: ZIP
* **output_evaluation_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_caprieval.zip). Accepted formats: ZIP
* **** (*string*): Path to the input PDB file containing an structure for reference. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_1GGR.pdb). Accepted formats: PDB
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_capri_eval.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
capri_eval --config config_capri_eval.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_evaluation_zip_path ref_caprieval.zip -- e2a-hpr_1GGR.pdb --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_capri_eval.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
capri_eval --config config_capri_eval.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_evaluation_zip_path ref_caprieval.zip -- e2a-hpr_1GGR.pdb --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Flex_ref
Wrapper class for the Haddock FlexRef module.
### Get help
Command:
```python
flex_ref -h
```
    /bin/sh: flex_ref: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **refinement_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **** (*string*): Path to the input TBL file containing a list of restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_flex_ref.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
flex_ref --config config_flex_ref.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip -- e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_flex_ref.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
flex_ref --config config_flex_ref.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip -- e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Rigid_body
Wrapper class for the Haddock RigidBody module.
### Get help
Command:
```python
rigid_body -h
```
    /bin/sh: rigid_body: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **docking_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **** (*string*): Path to the input TBL file containing a list of restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_rigid_body.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
rigid_body --config config_rigid_body.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --docking_output_zip_path ref_rigidbody.zip -- e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_rigid_body.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
rigid_body --config config_rigid_body.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --docking_output_zip_path ref_rigidbody.zip -- e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Topology
Wrapper class for the Haddock Topology module.
### Get help
Command:
```python
topology -h
```
    /bin/sh: topology: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **** (*string*): Path to the input PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/hpr_ensemble.pdb). Accepted formats: PDB
* **mol1_output_top_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_mol1_top.zip). Accepted formats: ZIP
* **mol2_output_top_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_mol2_top.zip). Accepted formats: ZIP
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_topology.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
topology --config config_topology.yml -- hpr_ensemble.pdb --mol1_output_top_zip_path ref_mol1_top.zip --mol2_output_top_zip_path ref_mol2_top.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_topology.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
topology --config config_topology.json -- hpr_ensemble.pdb --mol1_output_top_zip_path ref_mol1_top.zip --mol2_output_top_zip_path ref_mol2_top.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Clust_fcc
Wrapper class for the Haddock ClustFCC module.
### Get help
Command:
```python
clust_fcc -h
```
    /bin/sh: clust_fcc: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip). Accepted formats: ZIP
* **output_cluster_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_clustfcc.zip). Accepted formats: ZIP
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/configuration.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_clust_fcc.yml)
```python
properties:
  binary_path: /Users/pau/anaconda3/envs/haddock3/bin/haddock3
  remove_tmp: false

```
#### Command line
```python
clust_fcc --config config_clust_fcc.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_cluster_zip_path ref_clustfcc.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_clust_fcc.json)
```python
{
  "properties": {
    "binary_path": "/Users/pau/anaconda3/envs/haddock3/bin/haddock3",
    "remove_tmp": false
  }
}
```
#### Command line
```python
clust_fcc --config config_clust_fcc.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_cluster_zip_path ref_clustfcc.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
