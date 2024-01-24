from setuptools import setup,find_namespace_packages

setup(
    name='core_measures',
    install_requires=[
        "healdata-utils",
        "streamlit",
        "frictionless==4.40.8",
        "xlsxwriter",
        "openpyxl",
        
    ],
    package_dir={'': '.'},
    packages=find_namespace_packages(where='.')
)