# Biobb haddock changelog

## Unreleased

## What's new in version [5.4.0](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.4.0)?

### Changes

* [UPDATE] Update to biobb_common 5.4.0.
* [UPDATE] haddock3_run docs and JSON schema: the `global_cfg` property (HADDOCK3 global parameters, `{"postprocess": True}` by default) is documented; the block already used it.
* [FIX] topology: `mol1_output_top_zip_path` can be left out, as documented; the block failed without it.
* [FIX] haddock3_accessibility: the `probe_radius` property now reaches haddock3-restraints. It was ignored, so the accessibility was always computed with a 1.4 Å probe.
* [FIX] topology: a single molecule (no `mol2_input_pdb_path`) and a run without `mol2_output_top_zip_path` work; the block zipped the second molecule whenever `mol1_output_top_zip_path` was given and failed.
* [FIX] haddock3_passive_from_active: the residues of `input_active_list_path` reach haddock3-restraints (the command got an empty list), `surface_list_path` works (it raised a `KeyError`) and the `radius` property is passed.
* [FIX] haddock3_actpass_to_ambig: `pass_to_act` works. It rewrote the staged input files (the user's files with `disable_sandbox`) with an extra empty line, which haddock3 2025.11 rejects; the residues are now swapped in temporary copies. `pass_to_act` is documented.
* [FIX] HADDOCK3 step blocks: with an output folder of the same name as the input folder, the step folders of the input folder are no longer renamed before the run (`0_topoaa` to `00_topoaa`); the ones haddock3 renumbers are renamed in the output folder, also in `data/`.
* [FIX] haddock3_accessibility no longer deletes the `*.actpass` files of the folder it runs from.
* [UPDATE] `container_working_dir` removed from the docs and the JSON schemas: the commands run in the sandbox, mounted in `container_volume_path` in containers.
* [UPDATE] Python 3.11 to 3.13.

## What's new in version [5.3.3](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.3.3)?

### Changes

* [FIX] capri_eval: the `reference_pdb_path` structure now reaches HADDOCK3 as the caprieval reference. It was dropped, so models were scored against the best-scoring model instead of the given reference.
* [FIX] haddock3_passive_from_active, haddock3_actpass_to_ambig, haddock3_restrain_bodies, haddock3_accessibility and haddock_interface: stderr of the HADDOCK3 tools no longer ends up in the output files (warnings printed by the tools corrupted the restraint and actpass files); it goes to the error log instead.
* [FIX] topology docs and JSON schema: `output_haddock_wf_data` also accepts a directory (format `directory`), as the other HADDOCK3 blocks; the block already wrote the run folder for a path without the `.zip` extension.
* [UPDATE] README: readthedocs badge.

## What's new in version [5.3.2](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.3.2)?

### Changes

* [FEATURE] New restart_from property in haddock3_run, maps to the HADDOCK3 --restart option to resume or overwrite an existing run_dir.
* [UPDATE] Rename the anarcii block to biobb_anarcii (module `biobb_haddock.utils.biobb_anarcii`, command `biobb_anarcii`): its `anarcii` command clashed with the command of the ANARCII package it wraps, so the biocontainer ran ANARCII's CLI. `biobb_haddock.utils.anarcii` still imports it.
* [UPDATE] The conda package and the biocontainer use haddock_biobb 2025.11 compiled from source (linux-64), so the haddock3 blocks run in the biocontainer.
* [FIX] haddock_interface docs: the default `binary_path` is `haddock-restraints`.
* [FIX] biobb_anarcii JSON schema: ANARCII license written as `BSD 3-Clause`, as the biobb JSON master schema expects.

## What's new in version [5.3.1](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.3.1)?

### Changes

* [UPDATE] Fix anarcii imports.

## What's new in version [5.3.0](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.3.0)?

### Changes

* [UPDATE] Update to biobb_common 5.3.1
* [FEATURE] Add new blocks: haddock_interface, anarcii.

## What's new in version [5.2.1](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.2.1)?

### Changes

* [UPDATE] Update to biobb_common 5.2.2

## What's new in version [5.2.0](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.2.0)?

### Changes

* [UPDATE] Update to biobb_common 5.2.0

## What's new in version [5.1.1](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.1.1)?

### New features

* [UPDATE]: Use biobb_common 5.1.1
* [FEATURE]: Use input/output folders as arguments instead of zip folders.

## What's new in version [5.1.0](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.1.0)?

### New features

* [UPDATE]: Use haddock3 2025.5
* [FEAT]: Add global_cfg to properties.
* [FIX](https://github.com/bioexcel/biobb_haddock/issues/4): Extend pipe terminal compatibility.

## What's new in version [5.0.1](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.0.1)?

### New features

* New blocks for contact_map, haddock3_extend and haddock3_run.
* New restrain blocks: haddock3_accessibility, haddock3_actpass_to_ambig, haddock3_passive_from_active, haddock3_restrain_bodies.

### Changes

* Remove CNS installation need.

## What's new in version [5.0.0](https://github.com/bioexcel/biobb_haddock/releases/tag/v5.0.0)?

### Changes

* [CI/CD](env.yaml): Update biobb_common version.
* [CI/CD](linting_and_testing.yml): Update set-up micromamba.
* [Typing](ALL): Update typing from python 3.8 style to python 3.9
* [CI/CD](conf.yml): Adding global properties to test yaml configuration
* [CI/CD](GITIGNORE): Update .gitignore to include the new file extensions to ignore
* [CI/CD](conf.yml): Change test conf.yml to adapt to new settings configuration
* [FEATURE] New sandbox_path property

## What's new in version [4.2.1](https://github.com/bioexcel/biobb_haddock/releases/tag/4.2.1)?
First producction ready version of biobb_haddock

## What's new in version [4.1.0](https://github.com/bioexcel/biobb_haddock/releases/tag/4.1.0)?
First version of biobb_haddock

### New features
* New block for topologies

### Bug fixes

### Other changes
