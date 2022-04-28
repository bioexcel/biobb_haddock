# Install Haddock & CNS

# Haddock3

## 1 Clone the Haddock3 repository
Mind the `--recursive` flag when cloning!

```bash
git clone --recursive https://github.com/haddocking/haddock3.git
cd haddock3
cd src/fcc/src
chmod u+x Makefile
make
cd -
```

By the end of the above commands, you should be back to the `haddock3`
main folder.

## 2 Create a conda environment with Python 3.9+ and install dependencies:

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3
conda env create -f requirements.yml
conda activate haddock3
```

## 3 Install the HADDOCK3 package and command line clients

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3
python setup.py develop --no-deps
```

# CNS

## 1 Download the source code of CNS

In this case: `cns_solve_1.3_all.tar.gz`

From the [CNS site](http://cns-online.org) create a new folder in the Haddock
folder and uncompress it.

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3
mkdir haddock3/CNS
cp cns_solve_1.3_all.tar.gz haddock3/CNS/
cd haddock3/CNS/
tar xvzf cns_solve_1.3_all.tar.gz
```
## 2 Download the Intel Fortran and C++ offline compilers

In this case: `m_fortran-compiler-classic_p_2022.0.0.63_offline.dmg` and `m_cpp-compiler-classic_p_2022.0.0.62_offline.dmg`

From the [Intel developers site](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html) and double click to install them.

## 3 Configure the CNS environment

### 3.1 `cns_solve_env`:

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3/CNS
vim cns_solve_1.3/cns_solve_env
```
Modify the `CNS_SOLVE` env var:

```bash
# CHANGE THE NEXT LINE TO POINT TO THE LOCATION OF THE CNSsolve DIRECTORY

            setenv CNS_SOLVE '_CNSsolve_location_'

#
# ==========================================================================
```

In this case:

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.

            setenv CNS_SOLVE '/__PATH__/__to__/haddock3/CNS/cns_solve_1.3/'

```

### 3.2 `rtf.inc`:

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3/CNS
vim cns_solve_1.3/source/rtf.inc
```

Modify all the MX (maximum) variables adding one extra zero to all of them:
```
PARAMETER (MXRTRS=200,NICM=50) --> PARAMETER (MXRTRS=2000,NICM=50)
PARAMETER (MXRTA=2000)         --> PARAMETER (MXRTA=20000)
PARAMETER (MXRTX=2000)         --> PARAMETER (MXRTX=20000)
PARAMETER (MXRTB=2000)         --> PARAMETER (MXRTB=20000)
PARAMETER (MXRTT=3000)         --> PARAMETER (MXRTT=30000)
PARAMETER (MXRTP=2000)         --> PARAMETER (MXRTP=20000)
PARAMETER (MXRTI=2000)         --> PARAMETER (MXRTI=20000)
```

## 4 Compile and link CNS

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3/CNS/cns_solve_1.3
make install
```

If everything ended well, one of the last output lines will be:

```
created executable file cns_solve-xxxxxxxxx.exe
```

The `xxxxxxxxx` will be a different number on each build.

Finally link the CNS binary:

```bash
# Replace /__PATH__/__to__/ by your path to the haddock3 directory.
cd /__PATH__/__to__/haddock3
mkdir -p bin/
#Replace the  `xxxxxxxxx` and the __PATH__TO_BIN__ by your binary file
ln -s CNS/__PATH__TO_BIN__/cns_solve-xxxxxxxxx.exe bin/cns
```
