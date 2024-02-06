[![](https://img.shields.io/github/v/tag/bioexcel/biobb_haddock?label=Version)](https://GitHub.com/bioexcel/biobb_haddock/tags/)
[![](https://img.shields.io/pypi/v/biobb-haddock.svg?label=Pypi)](https://pypi.python.org/pypi/biobb-haddock/)
[![](https://img.shields.io/conda/vn/bioconda/biobb_haddock?label=Conda)](https://anaconda.org/bioconda/biobb_haddock)
[![](https://img.shields.io/conda/dn/bioconda/biobb_haddock?label=Conda%20Downloads)](https://anaconda.org/bioconda/biobb_haddock)
[![](https://img.shields.io/badge/Docker-Quay.io-blue)](https://quay.io/repository/biocontainers/biobb_haddock?tab=tags)
[![](https://img.shields.io/badge/Singularity-GalaxyProject-blue)](https://depot.galaxyproject.org/singularity/biobb_haddock:4.1.0--pyhdfd78af_0)

[![](https://img.shields.io/badge/OS-Unix%20%7C%20MacOS-blue)](https://github.com/bioexcel/biobb_haddock)
[![](https://img.shields.io/pypi/pyversions/biobb-haddock.svg?label=Python%20Versions)](https://pypi.org/project/biobb-haddock/)
[![](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![](https://img.shields.io/badge/Open%20Source%3f-Yes!-blue)](https://github.com/bioexcel/biobb_haddock)

[![](https://readthedocs.org/projects/biobb-haddock/badge/?version=latest&label=Docs)](https://biobb-haddock.readthedocs.io/en/latest/?badge=latest)
[![](https://img.shields.io/website?down_message=Offline&label=Biobb%20Website&up_message=Online&url=https%3A%2F%2Fmmb.irbbarcelona.org%2Fbiobb%2F)](https://mmb.irbbarcelona.org/biobb/)
[![](https://img.shields.io/badge/Youtube-tutorial-blue?logo=youtube&logoColor=red)](https://www.youtube.com/watch?v=ou1DOGNs0xM)
[![](https://zenodo.org/badge/DOI/10.1038/s41597-019-0177-4.svg)](https://doi.org/10.1038/s41597-019-0177-4)
[![](https://img.shields.io/endpoint?color=brightgreen&url=https%3A%2F%2Fapi.juleskreuer.eu%2Fcitation-badge.php%3Fshield%26doi%3D10.1038%2Fs41597-019-0177-4)](https://www.nature.com/articles/s41597-019-0177-4#citeas)

[![](https://docs.bioexcel.eu/biobb_haddock/junit/testsbadge.svg)](https://docs.bioexcel.eu/biobb_haddock/junit/report.html)
[![](https://docs.bioexcel.eu/biobb_haddock/coverage/coveragebadge.svg)](https://docs.bioexcel.eu/biobb_haddock/coverage/)
[![](https://docs.bioexcel.eu/biobb_haddock/flake8/flake8badge.svg)](https://docs.bioexcel.eu/biobb_haddock/flake8/)
[![](https://img.shields.io/github/last-commit/bioexcel/biobb_haddock?label=Last%20Commit)](https://github.com/bioexcel/biobb_haddock/commits/master)
[![](https://img.shields.io/github/issues/bioexcel/biobb_haddock.svg?color=brightgreen&label=Issues)](https://GitHub.com/bioexcel/biobb_haddock/issues/)

# biobb_haddock

### Introduction
biobb_haddock is the Biobb module collection to compute information-driven flexible protein-protein docking.
Biobb (BioExcel building blocks) packages are Python building blocks that
create new layer of compatibility and interoperability over popular
bioinformatics tools.
The latest documentation of this package can be found in our readthedocs site:
[latest API documentation](http://biobb-haddock.readthedocs.io/en/latest/).

### Version
v4.1.0 2024.1

### Installation
Using PIP:

> **Important:** PIP only installs the package. All the dependencies must be installed separately. To perform a complete installation, please use ANACONDA, DOCKER or SINGULARITY.

* Installation:


        pip install "biobb_haddock>=4.1.0"


* Usage: [Python API documentation](https://biobb-haddock.readthedocs.io/en/latest/modules.html)

Using ANACONDA:

* Installation:


        conda install -c bioconda "biobb_haddock>=4.1.0"


* Usage: With conda installation BioBBs can be used with the [Python API documentation](https://biobb-haddock.readthedocs.io/en/latest/modules.html) and the [Command Line documentation](https://biobb-haddock.readthedocs.io/en/latest/command_line.html)

Using DOCKER:

* Installation:


        docker pull quay.io/biocontainers/biobb_haddock:4.1.0--pyhdfd78af_0


* Usage:


        docker run quay.io/biocontainers/biobb_haddock:4.1.0--pyhdfd78af_0 <command>


Using SINGULARITY:

**MacOS users**: it's strongly recommended to avoid Singularity and use **Docker** as containerization system.

* Installation:


        singularity pull --name biobb_haddock.sif shub://bioexcel/biobb_haddock


* Usage:


        singularity exec biobb_haddock.sif <command>


The command list and specification can be found at the [Command Line documentation](https://biobb-haddock.readthedocs.io/en/latest/command_line.html).


### Copyright & Licensing
This software has been developed in the [MMB group](http://mmb.irbbarcelona.org) at the [BSC](http://www.bsc.es/) & [IRB](https://www.irbbarcelona.org/) for the [European BioExcel](http://bioexcel.eu/), funded by the European Commission (EU H2020 [823830](http://cordis.europa.eu/projects/823830), EU H2020 [675728](http://cordis.europa.eu/projects/675728)), EU Horizon Europe [101093290] (https://cordis.europa.eu/project/id/101093290).

* (c) 2015-2024 [Barcelona Supercomputing Center](https://www.bsc.es/)
* (c) 2015-2024 [Institute for Research in Biomedicine](https://www.irbbarcelona.org/)

Licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), see the file LICENSE for details.

![](https://bioexcel.eu/wp-content/uploads/2019/04/Bioexcell_logo_1080px_transp.png "Bioexcel")
