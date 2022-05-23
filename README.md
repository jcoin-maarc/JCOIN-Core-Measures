# JCOIN Frictionless Table Schemas/Data Dictionaries

Note: In development is the interactive "codebook", the data dictionary excel formatting (eg merging cells with redundant info like Section and subsection question text) detailed explanations of the:

- work flow (and how to contribute to this project)
- description/diagram of the data model structure (i.e., why did we separate into 'baseline' and 'time point' schemas and why did we add non-core-measures like visit_type or quarter enrolled?). 
    - These will be incorporated into this readme here and relevant portions will also be a part of the JDC documentation. These two items are sleighted to be complete by 5/27. 

- A few core measure sections in time point schema still need to be added including (a) MOUD  and (b) PROMIS and (c) Risk of harm and consequences
 

1. Manually fill out table schema spreadsheets in `csvs`
2. Clean up strings and convert to YAML table schemas with `make_core_measure_table_schemas.py`
    - originally converted to JSON to retain order\n but decided to switch to YAML to maintain consistency with other models
    - saved in `schemas`
3. Convert table schema fields to data dictionaries (ie easy-to-read reference of variables for each data set) with `make_data_dictionary.py`
    - saved in `data_dictionaries`




