# JCOIN Frictionless Table Schemas/Data Dictionaries

1. Fill out table schema spreadsheets in `csvs`
2. Clean up strings and convert to YAML table schemas with `make_core_measure_table_schemas.py`
    - originally converted to JSON to retain order\n but decided to switch to YAML to maintain consistency with other models
    - saved in `schemas`
3. Convert table schema fields to data dictionaries with `make_data_dictionary.py`
    - may be better off in jdc-docs but for now
    kept here and saved in `data_dictionaries`



