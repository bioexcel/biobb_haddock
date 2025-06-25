import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_haddock",
    version="5.1.0",
    author="Biobb developers",
    author_email="ruben.chaves@irbbarcelona.org",
    description="biobb_haddock is the Biobb module collection to compute information-driven flexible protein-protein docking.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_haddock",
    project_urls={
        "Documentation": "http://biobb_haddock.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/",
    },
    packages=setuptools.find_packages(exclude=["docs", "test"]),
    package_data={"biobb_haddock": ["py.typed"]},
    include_package_data=True,
    install_requires=["biobb_common==5.1.0"],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "capri_eval = biobb_haddock.haddock.capri_eval:main",
            "clust_fcc = biobb_haddock.haddock.clust_fcc:main",
            "contact_map = biobb_haddock.haddock.contact_map:main",
            "em_ref = biobb_haddock.haddock.em_ref:main",
            "flex_ref = biobb_haddock.haddock.flex_ref:main",
            "haddock3_extend = biobb_haddock.haddock.haddock3_extend:main",
            "haddock3_run = biobb_haddock.haddock.haddock3_run:main",
            "rigid_body = biobb_haddock.haddock.rigid_body:main",
            "sele_top_clusts = biobb_haddock.haddock.sele_top_clusts:main",
            "sele_top = biobb_haddock.haddock.sele_top:main",
            "topology = biobb_haddock.haddock.topology:main",
            "haddock3_accessibility = biobb_haddock.haddock_restraints.haddock3_accessibility:main",
            "haddock3_actpass_to_ambig = biobb_haddock.haddock_restraints.haddock3_actpass_to_ambig:main",
            "haddock3_passive_from_active = biobb_haddock.haddock_restraints.haddock3_passive_from_active:main",
            "haddock3_restrain_bodies = biobb_haddock.haddock_restraints.haddock3_restrain_bodies:main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
