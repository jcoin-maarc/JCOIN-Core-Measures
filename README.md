# JCOIN Frictionless Table Schemas/Data Dictionaries

The goal of this repository is to make data models for data validation and transformation in a frictionless format and use these to render human-readable data dictionaries consumable by analysts.


For more information on the frictionless data toolkit, [click here](https://frictionlessdata.io/)

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
        - note, this may be changed to from "baseline" to "person" in future to account for non-baseline measure in model (current enrollment status)
    2. Person/visit level: measures collected at all timepoints which is called `time-points`



# Notes and TODOs  

- integer encodings
    - Many software programs and analysts require or prefer integer encodings rather than string labels. To accommodate this across a wide range of software programs, the plan is to make a specification called "encodings" which will be mappings of integer encodings to variable values in data model.
    (we will also provide the outputted data files in various formats --- SPSS, SAS, Stata, RData, etc in future using this).
- consistency codes for missing values
    - eg skipped due to reason x, prefer not to answer and associated integer codes for these
    - ETA: 2022 Q2 JDC uploads
- user formatting for human readable data dictionary (eg freeze pane, etc)
- Fields left to add:
    - `MOUD for follow up measures` 
- file-level name changes
    - baseline measures to person 
- field/variable -level changes
    - currently for choice options, the choices are in front, depending on the group, it may be best to put these at end and with "choice=" text as is done in REDCAP etc.
- data model "entity" graph visualization
- fill out rest of `required` property

## Version history
- 1.0.0:
    upon putting all variables (besides MOUD follow up measures) into data model
- 1.1.0: 
    added shift_visit_dt to time points data model. for human-readable data dictionaries, added the variable "title" for easier look up and reference.