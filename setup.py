from setuptools import setup,find_namespace_packages

setup(
    name='core_measures',
    install_requires=[
        "streamlit-aggrid",
        "streamlit",
        "frictionless==4.40.8",
        "xlsxwriter"
    ],
    extras_require={
        'healdata_utils': ["healdata_utils @ git+https://github.com/norc-heal/healdata-utils.git"]
    },
    package_dir={'': '.'},
    packages=find_namespace_packages(where='.'),
    entry_points='''
        [console_scripts]
        schemas=core_measures.schemas:cli
    ''',
)