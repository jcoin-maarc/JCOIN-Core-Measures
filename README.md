# JCOIN Frictionless Table Schemas/Data Dictionaries


## Human readable data data dictionaries
`data_dictionaries` for spreadsheet format
and `codebooks` for an interactive codebook

Note: In development is the interactive "codebook", the data dictionary excel formatting (eg merging cells with redundant info like Section and subsection question text) detailed explanations of the:

## Steps to manually fill out csvs, make frictionless schemas, and make data dictionary
1. Manually fill out table schema spreadsheets in `csvs`
2. Clean up strings and convert to YAML table schemas with `make_core_measure_table_schemas.py`
    - originally converted to JSON to retain order\n but decided to switch to YAML to maintain consistency with other models
    - saved in `schemas`
3. Convert table schema fields to data dictionaries (ie easy-to-read reference of variables for each data set) with `make_data_dictionary.py`
    - saved in `data_dictionaries`


## Data model 

- We used an OMOP-consistent data model approach provides more flexibility in converting heterogenous hub source data into a common data model and is amenable to easier analyses

- Currently the two entities (ie., data objects) are: 
    1. Person level – measures collected only at baseline (and current enrollment status) which is called `baseline`
    2. Person/visit level: measures collected at all timepoints which is called `time-points`



# Notes    

- MOUD for follow up measures -- left out (lifetime MOUD measures are in baseline data model) as want to get input on this from JCOIN hubs.