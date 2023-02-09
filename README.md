# JCOIN Core Measures Table Schemas/Data Dictionaries

The goal of this repository is to make data models (ie schemas) and digestable products that allow
easier search and discovery of the JCOIN Core Measure variables for harmonization and analysis. 

For more information on the Table Schema specification used here, see the Frictionless Table Schema specification. Additionally,we conform to (and leverage tools from) the agreed upon HEAL initiative variable level metadata specifications and standards.

The schema/data dictionaries were created to represent (and build upon)
the publicly available core measures PDF document.


## Data model 

- We used an OMOP-consistent data model approach provides more flexibility in converting heterogenous hub source data into a common data model and is amenable to easier analyses

- Currently the two entities (ie., data objects) are: 
    1. Person level – measures collected only at baseline (and current enrollment status) which is called `baseline`
        - note, this may be changed to from "baseline" to "person" in future to account for non-baseline measure in model (current enrollment status)
    2. Person/visit level: measures collected at all timepoints which is called `time-points`

## Directories

The public repository where data dictionaries are stored is located [here](https://github.com/jcoin-maarc/JCOIN-Core-Measures). Below describes the directories in this repository:

`csvs`: tabular version of data dictionaries with standard frictionless names intended to conform to overall HEAL specifications.

`core_measures`: python modules (run `pip install -e .`)
    - `schemas.py`: simple CLI function to update csv files given updates to json files and vice versa. When using the `updatejson` option, minimally, there must be a schema json present with the same name stem (e.g., baseline.json) that contains at a minimum an empty json object but can also include schema-level properties such as a title and description. 
    - `app`: contains modules/fxns for the streamlit app (note -- the  `environment.yml` at root of repo is used for app deployment -- cannot have any base python packages)

> IMPORTANT: the source of truth for schemas are the schemas/*.json files (if the csv differs from the json file). However, the schemas.py script is intended to allow this json source of truth to be updated if using the csv to edit or update the schemas.

> The schemas were created using the publicly available JCOIN-core-measures-public.pdf document. Additionally, fields were added to satisfy additional fields for reporting such as quarter_enrolled, current_submission_status etc.

`encodings`: contains the mappings (ie value labels and missing value reserve codes) for translation to other software (e.g., SPSS and Stata). 

> NOTE: while schemas by definition do not contain any information used for transformations, we included the encodings here for easier editing and look up.

> NOTE: encodings in this context = value labels (e.g., 1=Male, 2=Female) and not the encoding of a file (e.g., utf-8)

`apps`: contains the multipage streamlit app making the variables and specifications easier to search and discover for harmonization and analysis.

## Version history (this list is no longer updated as we will now use tags)
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
