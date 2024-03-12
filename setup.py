from setuptools import setup,find_namespace_packages

setup(
    name='core_measures',
    install_requires=[
        "https://github.com/norc-heal/healdata-utils.git@848939fcf8de41d0462efa922fa30c4273a84a94",
        "streamlit",
        "frictionless==4.40.8",
        "xlsxwriter",
        "openpyxl",
        
    ],
    package_dir={'': '.'},
    packages=find_namespace_packages(where='.')
)