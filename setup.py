import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_haddock",
    version="3.8.0",
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
    install_requires=['biobb_common==3.8.0'],
    python_requires='==3.7.*',
    entry_points={
        "console_scripts": [
            "haddock = biobb_haddock.haddock.haddock:main"
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
