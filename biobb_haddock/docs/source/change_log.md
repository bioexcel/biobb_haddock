# Biobb haddock changelog

## Unreleased

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
