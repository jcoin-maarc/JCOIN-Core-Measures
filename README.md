# JCOIN Frictionless Table Schemas/Data Dictionaries

The goal of this repository is to make data models for data validation and transformation in a frictionless format and use these to render human-readable data dictionaries consumable by analysts.


For more information on the frictionless data toolkit, [click here](https://frictionlessdata.io/)

## Human readable data data dictionaries
See archive for previous versions. See github issues for future planned work.

## Schemas and data dictionaries

> WARNING: while the content will not change dramatically some of the scripts will to make this process more efficient.

`csvs`: tabular version of data dictionaries.
`make_core_measure_table_schemas.py`: converts to JSON schema (which is saved in `schemas`)

## Encoding transforms

`encodings`: contains the mappings (ie value labels and missing value reserve codes) for translation to other software (e.g., SPSS and Stata). 

> NOTE: while schemas by definition do not contain any information used for transformations, we included the encodings here for easier editing and look up.

> NOTE: encodings in this context = value labels (e.g., 1=Male, 2=Female) and not the encoding of a file (e.g., utf-8)

## Data model 

- We used an OMOP-consistent data model approach provides more flexibility in converting heterogenous hub source data into a common data model and is amenable to easier analyses

- Currently the two entities (ie., data objects) are: 
    1. Person level – measures collected only at baseline (and current enrollment status) which is called `baseline`
        - note, this may be changed to from "baseline" to "person" in future to account for non-baseline measure in model (current enrollment status)
    2. Person/visit level: measures collected at all timepoints which is called `time-points`


## Version history
- 1.0.0:
    upon putting all variables (besides MOUD follow up measures) into data model
- 1.1.0: 
    added shift_visit_dt to time points data model. for human-readable data dictionaries, added the variable "title" for easier look up and reference.
    Version 1.3.0 of schemas
- 1.2.0
    Major
    - for boolean columns (and string columns with Yes/No added: added trueValues and falseValues
    Minor
    - added missing demographic fields
    - corrected typos
