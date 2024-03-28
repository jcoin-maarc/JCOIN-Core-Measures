--8<-- [start:intro]

# JCOIN Core Measures Table Schemas/Data Dictionaries

 
This project builds data dictionaries (ie schemas) to represent (and build upon) the publicly available core measures PDF document. The goal of this project is to make machine readable data dictionaries and user-friendly products, allowing easier search and discovery of the JCOIN Core Measure variables for harmonization,analysis, and collaboration. 


## Data model 

- We used an OMOP-consistent data model approach provides more flexibility in converting heterogenous hub source data into a common data model and is amenable to easier analyses

- Currently the two entities (ie., data tables/files) are*: 
    1. Person level – measures collected only at baseline (and current enrollment status) which is called `baseline`
        - note, this may be changed to from "baseline" to "person" in future to account for non-baseline measure in model (current enrollment status)
    2. Person/visit level: measures collected at all timepoints which is called `time-points`


* staff also have baseline and time-points. While most staff will only have one timepoint, we put staff specific items that may be collected across timepoints (eg organizational questions), in `staff-timepoints`


## Data package standards (Frictionless) framework

The frictionless framework plays a foundational component in our Core Measures, both in building upon the core measures and building core measure data packages. For more information on frictionless standards, [click here](https://specs.frictionlessdata.io/). Specifically, the core measure data dictionary relies heavily on the [Table Schema specification](https://specs.frictionlessdata.io/table-schema).


## HEAL variable level metadata (vlmd) specifications

Our schemas were also designed to be compliant with [HEAL data ecosystem vlmd standards](https://github.com/HEAL/heal-metadata-schemas/tree/main/variable-level-metadata-schema). 


## Core Measure browser

To search the complete set of core measures and download a formatted excel version, click here(https://jcoin-maarc.github.io/JCOIN-Core-Measures/search-tool/). This provides a way to explore the most up-to-date data dictionaries and other dataset metadata properties such as missing values, descriptions, keys, etc.

--8<-- [end:intro]


## Contributing

- To contribute to the Core Measure schemas, modify the schemas/dictionary/*.yaml files

## Directories

The public repository where data dictionaries are stored is located [here](https://github.com/jcoin-maarc/JCOIN-Core-Measures). Below describes the directories in this repository:

### `csvs`: tabular version of data dictionaries with standard frictionless names intended to conform to overall HEAL specifications.

### `core_measures`: python modules (run `pip install -e .`) Contents are:

- `schemas.py`: simple CLI function to update csv files given updates to json files and vice versa. When using the `updatejson` option, minimally, there must be a schema json present with the same name stem (e.g., baseline.json) that contains at a minimum an empty json object but can also include schema-level properties such as a title and description. 

- `app`: contains modules/fxns for the streamlit app (note -- the  `environment.yml` at root of repo is used for app deployment -- cannot have any base python packages)

> IMPORTANT: the source of truth for schemas are the schemas/*.json files (if the csv differs from the json file). However, the schemas.py script is intended to allow this json source of truth to be updated if using the csv to edit or update the schemas.

> The schemas were created using the publicly available JCOIN-core-measures-public.pdf document. Additionally, fields were added to satisfy additional fields for reporting such as quarter_enrolled, current_submission_status etc.

### `encodings`: contains the mappings (ie value labels and missing value reserve codes) for translation to other software (e.g., SPSS and Stata). 

> NOTE: while schemas by definition do not contain any information used for transformations, we included the encodings here for easier editing and look up.

> NOTE: encodings in this context = value labels (e.g., 1=Male, 2=Female) and not the encoding of a file (e.g., utf-8)

### `app`: contains the streamlit app code making the variables and specifications easier to search and discover for harmonization and analysis.

## Schema version history 
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
- 1.3.0b
    Added staff schemas (both baseline and "time-points")
- 2.0.0
    Added new variable names with more semantic meaning describing variable. The original names are kept in `custom.jcoin:original_name`
    for ease of interoperatability. 
- 2.0.1 (5/31/2023)
    Added `visit_month` field.
- 2.1.0
    Minor additional annotations; added `hub_id`; incorporated combined race variable
- 2.2.0 
    - Added `days_on_study`
    - Removed `required` constraint from `shifted_visit_date` while making note either `days_on_study` or `shifted_visit_date` is acceptable.
    - Added `Not collected` to `missingValues` to differentiate Missing from `Not collected`
    - Changed `current_study_status` to add withdrawn due to re-incarceration and deceased. 
