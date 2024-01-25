import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_haddock",
    version="4.1.0",
    author="Biobb developers",
    author_email="pau.andrio@bsc.es",
    description="biobb_haddock is the Biobb module collection to compute information-driven flexible protein-protein docking.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_haddock",
    project_urls={
        "Documentation": "http://biobb_haddock.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['docs', 'test']),
    include_package_data=True,
    install_requires=['biobb_common==3.8.1'],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "haddock = biobb_haddock.haddock.capri_eval:main",
            "haddock = biobb_haddock.haddock.clust_fcc:main",
            "haddock = biobb_haddock.haddock.em_ref:main",
            "haddock = biobb_haddock.haddock.flex_ref:main",
            "haddock = biobb_haddock.haddock.rigid_body:main",
            "haddock = biobb_haddock.haddock.sele_top:main",
            "haddock = biobb_haddock.haddock.topology:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ],
)
