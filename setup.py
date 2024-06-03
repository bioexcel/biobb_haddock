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
    install_requires=['biobb_common==4.1.0'],
    python_requires='>=3.9',
    entry_points={
        "console_scripts": [
            "capri_eval = biobb_haddock.haddock.capri_eval:main",
            "clust_fcc = biobb_haddock.haddock.clust_fcc:main",
            "em_ref = biobb_haddock.haddock.em_ref:main",
            "flex_ref = biobb_haddock.haddock.flex_ref:main",
            "rigid_body = biobb_haddock.haddock.rigid_body:main",
            "sele_top = biobb_haddock.haddock.sele_top:main",
            "topology = biobb_haddock.haddock.topology:main"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix"
    ],
)
