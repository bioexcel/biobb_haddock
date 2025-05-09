# BioBB HADDOCK Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


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
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_caprieval.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
capri_eval --config config_capri_eval.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_evaluation_zip_path ref_caprieval.zip --reference_pdb_path e2a-hpr_1GGR.pdb --output_haddock_wf_data_zip haddock_wf_data_caprieval.zip --haddock_config_path run.cfg
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
capri_eval --config config_capri_eval.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_evaluation_zip_path ref_caprieval.zip --reference_pdb_path e2a-hpr_1GGR.pdb --output_haddock_wf_data_zip haddock_wf_data_caprieval.zip --haddock_config_path run.cfg
```

## Flex_ref
Wrapper class for the Haddock FlexRef module.
### Get help
Command:
```python
flex_ref -h
```
    usage: flex_ref [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH [--ambig_restraints_table_path AMBIG_RESTRAINTS_TABLE_PATH] [--unambig_restraints_table_path UNAMBIG_RESTRAINTS_TABLE_PATH] [--hb_restraints_table_path HB_RESTRAINTS_TABLE_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock FlexRef module.
    
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
      --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **refinement_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **ambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **unambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **hb_restraints_table_path** (*string*): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
flex_ref --config config_flex_ref.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
flex_ref --config config_flex_ref.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
rigid_body --config config_rigid_body.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --docking_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
rigid_body --config config_rigid_body.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --docking_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```

## Haddock3_passive_from_active
Wrapper class for the Haddock3-Restraints passive_from_active module.
### Get help
Command:
```python
haddock3_passive_from_active -h
```
    usage: haddock3_passive_from_active [-h] [-c CONFIG] --input_pdb_path INPUT_PDB_PATH --output_actpass_path OUTPUT_ACTPASS_PATH [--input_active_list_path INPUT_ACTIVE_LIST_PATH]
    
    Wrapper of the haddock3-restraints passive_from_active module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --input_active_list_path INPUT_ACTIVE_LIST_PATH
    
    required arguments:
      --input_pdb_path INPUT_PDB_PATH
      --output_actpass_path OUTPUT_ACTPASS_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_pdb_path** (*string*): Path to the input PDB structure file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/1A2P_ch.pdb). Accepted formats: PDB
* **output_actpass_path** (*string*): Path to the output file with list of passive residues. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/1A2P_manual_actpass.txt). Accepted formats: TXT, DAT, LIST, OUT
* **input_active_list_path** (*string*): Path to the input file with list of active residues. File type: input. [Sample file](None). Accepted formats: TXT, DAT, LIST, ACTIVE_LIST
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **active_list** (*string*): () List of active residues as a comma-separated string. Required if input_active_list_path is not provided..
* **chain_id** (*string*): (None) Chain ID to consider when calculating passive residues..
* **surface_list_path** (*string*): () Path to file with list of surface residues to filter..
* **radius** (*number*): (6.5) Radius in Angstroms to look for surface residues around active ones..
* **binary_path** (*string*): (haddock3-restraints) Path to the haddock3-restraints executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_passive_from_active.yml)
```python
properties:
  active_list: 27,73,83,87
  remove_tmp: false

```
#### Command line
```python
haddock3_passive_from_active --config config_haddock3_passive_from_active.yml --input_pdb_path 1A2P_ch.pdb --output_actpass_path 1A2P_manual_actpass.txt --input_active_list_path input.txt
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_passive_from_active.json)
```python
{
  "properties": {
    "remove_tmp": false,
    "active_list": "27,73,83,87"
  }
}
```
#### Command line
```python
haddock3_passive_from_active --config config_haddock3_passive_from_active.json --input_pdb_path 1A2P_ch.pdb --output_actpass_path 1A2P_manual_actpass.txt --input_active_list_path input.txt
```

## Sele_top_clusts
Wrapper class for the Haddock SeleTopClusts module.
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
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
sele_top_clusts --config config_sele_top_clusts.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
sele_top_clusts --config config_sele_top_clusts.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```

## Haddock3_run
Wrapper class for the Haddock3 run module.
### Get help
Command:
```python
haddock3_run -h
```
    usage: haddock3_run [-h] [-c CONFIG] --mol1_input_pdb_path MOL1_INPUT_PDB_PATH --mol2_input_pdb_path MOL2_INPUT_PDB_PATH --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP [--ambig_restraints_table_path AMBIG_RESTRAINTS_TABLE_PATH] [--unambig_restraints_table_path UNAMBIG_RESTRAINTS_TABLE_PATH] [--hb_restraints_table_path HB_RESTRAINTS_TABLE_PATH] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock3 HADDOCK3 module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --ambig_restraints_table_path AMBIG_RESTRAINTS_TABLE_PATH
      --unambig_restraints_table_path UNAMBIG_RESTRAINTS_TABLE_PATH
      --hb_restraints_table_path HB_RESTRAINTS_TABLE_PATH
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --mol1_input_pdb_path MOL1_INPUT_PDB_PATH
      --mol2_input_pdb_path MOL2_INPUT_PDB_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **mol1_input_pdb_path** (*string*): Path to the input PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G.pdb). Accepted formats: PDB
* **mol2_input_pdb_path** (*string*): Path to the input PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/hpr_ensemble.pdb). Accepted formats: PDB
* **ambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **unambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **hb_restraints_table_path** (*string*): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_run.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
haddock3_run --config config_haddock3_run.yml --mol1_input_pdb_path e2aP_1F3G.pdb --mol2_input_pdb_path hpr_ensemble.pdb --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_run.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
haddock3_run --config config_haddock3_run.json --mol1_input_pdb_path e2aP_1F3G.pdb --mol2_input_pdb_path hpr_ensemble.pdb --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_clustfcc.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
clust_fcc --config config_clust_fcc.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_cluster_zip_path ref_clustfcc.zip --output_haddock_wf_data_zip haddock_wf_data_clustfcc.zip --haddock_config_path run.cfg
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
clust_fcc --config config_clust_fcc.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_cluster_zip_path ref_clustfcc.zip --output_haddock_wf_data_zip haddock_wf_data_clustfcc.zip --haddock_config_path run.cfg
```

## Haddock3_accessibility
Wrapper class for the Haddock-Restraints Accessibility module.
### Get help
Command:
```python
haddock3_accessibility -h
```
    usage: haddock3_accessibility [-h] [-c CONFIG] --input_pdb_path INPUT_PDB_PATH --output_accessibility_path OUTPUT_ACCESSIBILITY_PATH [--output_actpass_path OUTPUT_ACTPASS_PATH]
    
    Wrapper of the haddock-restraints Accessibility module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --output_actpass_path OUTPUT_ACTPASS_PATH
    
    required arguments:
      --input_pdb_path INPUT_PDB_PATH
      --output_accessibility_path OUTPUT_ACCESSIBILITY_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_pdb_path** (*string*): Path to the input PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2aP_1F3G_noH.pdb). Accepted formats: PDB
* **output_accessibility_path** (*string*): Path to the output file with accessibility information. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/mol1_sasa.txt). Accepted formats: TXT, DAT, OUT
* **output_actpass_path** (*string*): Path to the output file with active/passive residues to be used as haddock3 restraint information. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/mol1_haddock_actpass.txt). Accepted formats: TXT, DAT, OUT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **chain** (*string*): (A) Chain to be used from the input PDB file..
* **cutoff** (*number*): (0.4) Relative cutoff for sidechain accessibility..
* **probe_radius** (*number*): (1.4) Probe radius for the accessibility calculation..
* **pass_to_act** (*boolean*): (False) If True, the passive residues become active in the actpass file and vice versa..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_accessibility.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
haddock3_accessibility --config config_haddock3_accessibility.yml --input_pdb_path e2aP_1F3G_noH.pdb --output_accessibility_path mol1_sasa.txt --output_actpass_path mol1_haddock_actpass.txt
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_accessibility.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
haddock3_accessibility --config config_haddock3_accessibility.json --input_pdb_path e2aP_1F3G_noH.pdb --output_accessibility_path mol1_sasa.txt --output_actpass_path mol1_haddock_actpass.txt
```

## Sele_top
Wrapper class for the Haddock SeleTop module.
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
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
sele_top --config config_sele_top.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
sele_top --config config_sele_top.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_selection_zip_path ref_seletop.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```

## Em_ref
Wrapper class for the Haddock EMRef module.
### Get help
Command:
```python
em_ref -h
```
    usage: em_ref [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH [--ambig_restraints_table_path AMBIG_RESTRAINTS_TABLE_PATH] [--unambig_restraints_table_path UNAMBIG_RESTRAINTS_TABLE_PATH] [--hb_restraints_table_path HB_RESTRAINTS_TABLE_PATH] [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock EMRef module.
    
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
      --refinement_output_zip_path REFINEMENT_OUTPUT_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_topology.zip). Accepted formats: ZIP
* **refinement_output_zip_path** (*string*): Path to the output PDB file collection in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_rigidbody.zip). Accepted formats: ZIP
* **ambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of ambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **unambig_restraints_table_path** (*string*): Path to the input TBL file containing a list of unambiguous restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **hb_restraints_table_path** (*string*): Path to the input TBL file containing a list of hydrogen bond restraints for docking. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/e2a-hpr_air.tbl). Accepted formats: TBL
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
em_ref --config config_em_ref.yml --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
em_ref --config config_em_ref.json --input_haddock_wf_data_zip haddock_wf_data_topology.zip --refinement_output_zip_path ref_rigidbody.zip --ambig_restraints_table_path e2a-hpr_air.tbl --unambig_restraints_table_path e2a-hpr_air.tbl --hb_restraints_table_path e2a-hpr_air.tbl --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```

## Haddock3_extend
Wrapper class for the Haddock3 extend module.
### Get help
Command:
```python
haddock3_extend -h
```
    usage: haddock3_extend [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --haddock_config_path HADDOCK_CONFIG_PATH --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
    
    Wrapper of the haddock3 HADDOCK3 module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_topology.zip). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_extend.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
haddock3_extend --config config_haddock3_extend.yml --input_haddock_wf_data_zip ref_topology.zip --haddock_config_path run.cfg --output_haddock_wf_data_zip ref_topology.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_extend.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
haddock3_extend --config config_haddock3_extend.json --input_haddock_wf_data_zip ref_topology.zip --haddock_config_path run.cfg --output_haddock_wf_data_zip ref_topology.zip
```

## Haddock3_actpass_to_ambig
Wrapper class for the Haddock-Restraints active_passive_to_ambig module.
### Get help
Command:
```python
haddock3_actpass_to_ambig -h
```
    usage: haddock3_actpass_to_ambig [-h] [-c CONFIG] --input_actpass1_path INPUT_ACTPASS1_PATH --input_actpass2_path INPUT_ACTPASS2_PATH --output_tbl_path OUTPUT_TBL_PATH
    
    Wrapper of the haddock-restraints active_passive_to_ambig module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_actpass1_path INPUT_ACTPASS1_PATH
      --input_actpass2_path INPUT_ACTPASS2_PATH
      --output_tbl_path OUTPUT_TBL_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_actpass1_path** (*string*): Path to the first input HADDOCK active-passive file containing active (in the first line) and passive (second line) residues. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/haddock_actpass1.txt). Accepted formats: TXT, DAT, IN, PASS
* **input_actpass2_path** (*string*): Path to the second input HADDOCK active-passive file containing active (in the first line) and passive (second line) residues. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/haddock_actpass2.txt). Accepted formats: TXT, DAT, IN, PASS
* **output_tbl_path** (*string*): Path to the output HADDOCK tbl file with Ambiguous Interaction Restraints (AIR) information. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/haddock_actpass.tbl). Accepted formats: TBL, TXT, OUT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pass_to_act** (*boolean*): (False) Path to the haddock haddock executable binary..
* **segid_one** (*string*): (None) Segid of the first model..
* **segid_two** (*string*): (None) Segid of the second model..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_actpass_to_ambig.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
haddock3_actpass_to_ambig --config config_haddock3_actpass_to_ambig.yml --input_actpass1_path haddock_actpass1.txt --input_actpass2_path haddock_actpass2.txt --output_tbl_path haddock_actpass.tbl
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_actpass_to_ambig.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
haddock3_actpass_to_ambig --config config_haddock3_actpass_to_ambig.json --input_actpass1_path haddock_actpass1.txt --input_actpass2_path haddock_actpass2.txt --output_tbl_path haddock_actpass.tbl
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
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
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
topology --config config_topology.yml --mol1_input_pdb_path e2aP_1F3G.pdb --mol1_output_top_zip_path ref_mol1_top.zip --mol2_input_pdb_path hpr_ensemble.pdb --mol2_output_top_zip_path ref_mol2_top.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
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
topology --config config_topology.json --mol1_input_pdb_path e2aP_1F3G.pdb --mol1_output_top_zip_path ref_mol1_top.zip --mol2_input_pdb_path hpr_ensemble.pdb --mol2_output_top_zip_path ref_mol2_top.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```

## Contact_map
Wrapper class for the Haddock ContactMap module.
### Get help
Command:
```python
contact_map -h
```
    usage: contact_map [-h] [-c CONFIG] --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP --output_contactmap_zip_path OUTPUT_CONTACTMAP_ZIP_PATH [--output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP] [--haddock_config_path HADDOCK_CONFIG_PATH]
    
    Wrapper of the haddock ContactMap module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
      --output_haddock_wf_data_zip OUTPUT_HADDOCK_WF_DATA_ZIP
      --haddock_config_path HADDOCK_CONFIG_PATH
    
    required arguments:
      --input_haddock_wf_data_zip INPUT_HADDOCK_WF_DATA_ZIP
      --output_contactmap_zip_path OUTPUT_CONTACTMAP_ZIP_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_haddock_wf_data_zip** (*string*): Path to the input zipball containing all the current Haddock workflow data. File type: input. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_rigid.zip). Accepted formats: ZIP
* **output_contactmap_zip_path** (*string*): Path to the output contact map files in zip format. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock/ref_contactmap.zip). Accepted formats: ZIP
* **output_haddock_wf_data_zip** (*string*): Path to the output zipball containing all the current Haddock workflow data. File type: output. [Sample file](https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_emref.zip). Accepted formats: ZIP
* **haddock_config_path** (*string*): Haddock configuration CFG file path. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg). Accepted formats: CFG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cfg** (*object*): ({}) Haddock configuration options specification..
* **binary_path** (*string*): (haddock) Path to the haddock haddock executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_contact_map.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
contact_map --config config_contact_map.yml --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_contactmap_zip_path ref_contactmap.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_contact_map.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
contact_map --config config_contact_map.json --input_haddock_wf_data_zip haddock_wf_data_rigid.zip --output_contactmap_zip_path ref_contactmap.zip --output_haddock_wf_data_zip haddock_wf_data_emref.zip --haddock_config_path run.cfg
```

## Haddock3_restrain_bodies
Wrapper class for the Haddock-Restraints restrain_bodies module.
### Get help
Command:
```python
haddock3_restrain_bodies -h
```
    usage: haddock3_restrain_bodies [-h] [-c CONFIG] --input_structure_path INPUT_STRUCTURE_PATH --output_tbl_path OUTPUT_TBL_PATH
    
    Wrapper of the haddock-restraints restrain_bodies module.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_structure_path INPUT_STRUCTURE_PATH
      --output_tbl_path OUTPUT_TBL_PATH
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_structure_path** (*string*): Path to the input PDB structure to be restrained. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/4G6K_clean.pdb). Accepted formats: PDB
* **output_tbl_path** (*string*): Path to the output HADDOCK tbl file with Ambiguous Interaction Restraints (AIR) information. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/reference/haddock_restraints/antibody-unambig.tbl). Accepted formats: TBL, TXT, OUT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **exclude** (*string*): (None) Chains to exclude from the calculation..
* **verbose** (*integer*): (0) Tune verbosity of the output..
* **binary_path** (*string*): (haddock3-restraints) Path to the HADDOCK3 restraints executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Path to the binary executable of your container..
* **container_image** (*string*): (None) Container Image identifier..
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container..
* **container_working_dir** (*string*): (None) Path to the internal CWD in the container..
* **container_user_id** (*string*): (None) User number id to be mapped inside the container..
* **container_shell_path** (*string*): (/bin/bash) Path to the binary executable of the container shell..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_restrain_bodies.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
haddock3_restrain_bodies --config config_haddock3_restrain_bodies.yml --input_structure_path 4G6K_clean.pdb --output_tbl_path antibody-unambig.tbl
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_haddock/blob/master/biobb_haddock/test/data/config/config_haddock3_restrain_bodies.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
haddock3_restrain_bodies --config config_haddock3_restrain_bodies.json --input_structure_path 4G6K_clean.pdb --output_tbl_path antibody-unambig.tbl
```
