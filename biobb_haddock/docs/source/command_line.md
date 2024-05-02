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
    usage: em_ref [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH [--restraints_table_path RESTRAINTS_TABLE_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock EMRef module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --restraints_table_path RESTRAINTS_TABLE_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **refinement_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **restraints_table_path** (*string*): Path to the input TBL file containing a list of restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
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
  remove_tmp: false

```
#### Command line
```python
em_ref --config config_em_ref.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_em_ref.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
em_ref --config config_em_ref.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Sele_top
Wrapper class for the Haddock SeleTop module https://www.bonvinlab.org/haddock3/modules/analysis/seletop.html
### Get help
Command:
```python
sele_top -h
```
    usage: sele_top [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --output_selection_zip_path OUTPUT_SELECTION_ZIP_PATH [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock SeleTop module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --output_selection_zip_path OUTPUT_SELECTION_ZIP_PATH
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
    "remove_tmp": false
  }
}
```
#### Command line
```python
sele_top --config config_sele_top.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Sele_top_clusts
Wrapper class for the Haddock SeleTopClusts module https://www.bonvinlab.org/haddock3/modules/analysis/seletopclusts.html.
### Get help
Command:
```python
sele_top_clusts -h
```
    usage: sele_top_clusts [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --output_selection_zip_path OUTPUT_SELECTION_ZIP_PATH [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock SeleTopClusts module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --output_selection_zip_path OUTPUT_SELECTION_ZIP_PATH
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
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_sele_top_clusts.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
sele_top_clusts --config config_sele_top_clusts.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_sele_top_clusts.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
sele_top_clusts --config config_sele_top_clusts.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Capri_eval
Wrapper class for the Haddock CapriEval module.
### Get help
Command:
```python
capri_eval -h
```
    usage: capri_eval [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --output_evaluation_zip_path OUTPUT_EVALUATION_ZIP_PATH [--reference_pdb_path REFERENCE_PDB_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock CapriEval module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --reference_pdb_path REFERENCE_PDB_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --output_evaluation_zip_path OUTPUT_EVALUATION_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip). Accepted formats: ZIP
* **output_evaluation_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_caprieval.zip). Accepted formats: ZIP
* **reference_pdb_path** (*string*): Path to the input PDB file containing an structure for reference. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_1GGR.pdb). Accepted formats: PDB
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
  remove_tmp: false

```
#### Command line
```python
capri_eval --config config_capri_eval.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_evaluation_zip_path ref_caprieval.zip --reference_pdb_path e2a-hpr_1GGR.pdb --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_capri_eval.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
capri_eval --config config_capri_eval.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_evaluation_zip_path ref_caprieval.zip --reference_pdb_path e2a-hpr_1GGR.pdb --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Flex_ref
Wrapper class for the Haddock FlexRef module.
### Get help
Command:
```python
flex_ref -h
```
    usage: flex_ref [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH [--restraints_table_path RESTRAINTS_TABLE_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock FlexRef module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --restraints_table_path RESTRAINTS_TABLE_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **refinement_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **restraints_table_path** (*string*): Path to the input TBL file containing a list of restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
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
  remove_tmp: false

```
#### Command line
```python
flex_ref --config config_flex_ref.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_flex_ref.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
flex_ref --config config_flex_ref.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Rigid_body
Wrapper class for the Haddock RigidBody module.
### Get help
Command:
```python
rigid_body -h
```
    usage: rigid_body [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --docking_output_zip_path DOCKING_OUTPUT_ZIP_PATH [--ambig_restraints_table_path AMBIG_RESTRAINTS_TABLE_PATH] [--unambig_restraints_table_path UNAMBIG_RESTRAINTS_TABLE_PATH] [--hb_restraints_table_path HB_RESTRAINTS_TABLE_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock RigidBody module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --ambig_restraints_table_path AMBIG_RESTRAINTS_TABLE_PATH
      --unambig_restraints_table_path UNAMBIG_RESTRAINTS_TABLE_PATH
      --hb_restraints_table_path HB_RESTRAINTS_TABLE_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --docking_output_zip_path DOCKING_OUTPUT_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **docking_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **ambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **unambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **hb_restraints_table_path** (*string*): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
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
  remove_tmp: false

```
#### Command line
```python
rigid_body --config config_rigid_body.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --docking_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_rigid_body.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
rigid_body --config config_rigid_body.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --docking_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Topology
Wrapper class for the Haddock Topology module.
### Get help
Command:
```python
topology -h
```
    usage: topology [-h] [-c CONFIG] --mol1_input_pdb_path MOL1_INPUT_PDB_PATH --mol1_output_top_zip_path MOL1_OUTPUT_TOP_ZIP_PATH [--mol2_input_pdb_path MOL2_INPUT_PDB_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--mol2_output_top_zip_path MOL2_OUTPUT_TOP_ZIP_PATH] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock haddock module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --mol2_input_pdb_path MOL2_INPUT_PDB_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --mol2_output_top_zip_path MOL2_OUTPUT_TOP_ZIP_PATH
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --mol1_input_pdb_path MOL1_INPUT_PDB_PATH
      --mol1_output_top_zip_path MOL1_OUTPUT_TOP_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **mol1_input_pdb_path** (*string*): Path to the input PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G.pdb). Accepted formats: PDB
* **mol1_output_top_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_mol1_top.zip). Accepted formats: ZIP
* **mol2_input_pdb_path** (*string*): Path to the input PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/hpr_ensemble.pdb). Accepted formats: PDB
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
  remove_tmp: false

```
#### Command line
```python
topology --config config_topology.yml --mol1_input_pdb_path e2aP_1F3G.pdb --mol1_output_top_zip_path ref_mol1_top.zip --mol2_input_pdb_path hpr_ensemble.pdb --mol2_output_top_zip_path ref_mol2_top.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_topology.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
topology --config config_topology.json --mol1_input_pdb_path e2aP_1F3G.pdb --mol1_output_top_zip_path ref_mol1_top.zip --mol2_input_pdb_path hpr_ensemble.pdb --mol2_output_top_zip_path ref_mol2_top.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```

## Clust_fcc
Wrapper class for the Haddock ClustFCC module.
### Get help
Command:
```python
clust_fcc -h
```
    usage: clust_fcc [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --output_cluster_zip_path OUTPUT_CLUSTER_ZIP_PATH [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock ClustFCC module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --output_cluster_zip_path OUTPUT_CLUSTER_ZIP_PATH
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
    "remove_tmp": false
  }
}
```
#### Command line
```python
clust_fcc --config config_clust_fcc.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_cluster_zip_path ref_clustfcc.zip --output_haddock_wf_data_zip ref_topology.zip --haddock_config_path configuration.cfg
```
