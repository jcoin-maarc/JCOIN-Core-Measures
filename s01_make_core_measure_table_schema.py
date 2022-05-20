''' 
converts a tabular flat frictionless schema
into a YAML file after cleaning up string columns

Goal of this step (rather than adding directly to a YAML)
is to expedite creation of schema by leveraging spreadsheet view
''' 

import os
import pandas as pd
import json
import yaml
from frictionless import validate_schema
from collections.abc import Iterable



#need to make sure dtypes are consistent with schema specs
#https://specs.frictionlessdata.io/table-schema/#types-and-formats
dtypes_columns = {
    "required":bool,
    "maxLength":int,
    "pattern":str,
    'enum':list,
}


def read_table_schema_spreadsheet(schema_path, delimiter=None):
    file, ext = os.path.splitext(schema_path)
    if ext == ".xlsx":
        return pd.read_excel(schema_path, engine="openpyxl").convert_dtypes()
    else:
        assert delimiter
        return pd.read_csv(schema_path, delimiter=delimiter).convert_dtypes()


def format_table_schema_df(
    tbl_schema_df,
    regex_of_custom_fields="^jcoin:|notes|^heal:",
    constraint_columns=['required','maxLength','pattern','required','enum'],
    fields=["name", "title","type", "description", "constraints", "custom"],
):
    """
    Formats a pandas dataframe table schema based on a very specific template

    currently constraints are nested as stringified JSON
    (in future will make separate columns)

    Parameters
    ------------
    df: input dataframe that has all columns necessary for table schema
    regex_of_custom_fields:

    regex_of_custom_fields: custom are separate columns (will make constraints same thing as custom)
    (for now enter regexs as parameter)

    fields: list of final fields to return if specificied

    Returns
    -------------
    df : formatted table schema
    """
    def _combine_cols_into_dict(df):
        return df.apply(lambda x: x.dropna().to_dict(),axis='columns')
    
    def _split_if_str(s,delimiter=','):
        if type(s) is str:
            return s.split(delimiter)
        else:
            return None

    for cols in tbl_schema_df.columns:
        #python 3.10 has diff string dtypes so just have to see if it has str method
        #print(tbl_schema_df[cols].dtype)
        if tbl_schema_df[cols].dtype.type is str:
            #print(cols + "is string") 
            tbl_schema_df[cols] = tbl_schema_df[cols].str.strip().str.replace('\n',' ')
    # combine custom columns
    custom = tbl_schema_df.filter(regex=regex_of_custom_fields).pipe(
        _combine_cols_into_dict)
    tbl_schema_df["custom"] = custom
    # combine constraint columns
    ## convert enum to list
    tbl_schema_df['enum'].update(tbl_schema_df['enum'].apply( _split_if_str))
    constraints = tbl_schema_df[constraint_columns].pipe(
        _combine_cols_into_dict
    )
    tbl_schema_df["constraints"] = constraints  # just reformatting so update
    if fields:
        return tbl_schema_df[fields]
    else:
        return tbl_schema_df


def convert_table_schema_df_to_dict(
    tbl_schema_df,
    primary_keys,
    foreign_keys=None,
    missing_values=["NaN", "NA", "", "."],
    table_description=None,
):
    """
    converts a pandas dataframe into a table schema dictionary and adds
    table schema level properties

    TODO: make more flexible in terms of table level specs to pass with kwargs

    Parameters
    ----------------
    tbl_schema_df: formatted table schema
    primary_keys : primary key defining unique observations

    Returns
    ----------------
    dict : table schema with table schema level properties added
    """
    # filter NaNs
    tbl_schema_dict = {}
    tbl_schema_dict["fields"] = [
        row.dropna().to_dict() for index, row in tbl_schema_df.iterrows()
    ]

    if primary_keys:
        tbl_schema_dict["primaryKey"] = primary_keys

    if missing_values:
        tbl_schema_dict["missingValues"] = missing_values

    if foreign_keys:
        tbl_schema_dict["foreignKeys"] = foreign_keys

    if table_description:
        tbl_schema_dict["description"] = table_description

    return tbl_schema_dict

if __name__ == "__main__":
    table_schemas = {
        "Baseline Fields: Measures collected only at baseline ": "table-schema-baseline",
        "Time point Fields: Measures collected at all time points (baseline and follow ups)": "table-schema-time-points",
    }


    for schema_description, schema_path in table_schemas.items():

        # format the flattened tabular table schema view
        spreadsheet_dir = os.path.join('csvs', f"{schema_path}.csv")
        tbl_schema_df = read_table_schema_spreadsheet(spreadsheet_dir,delimiter=',').pipe(
            format_table_schema_df
        )
        #tbl_schema_df.replace('\n','').to_csv(os.path.splitext(spreadsheet_dir)[0]+".tsv",sep='\t')
        if "baseline fields:" in schema_description.lower():
            primary_keys = ["jdc_person_id"]
            foreign_keys = None
        elif "time point fields:" in schema_description.lower():
            primary_keys = ["jdc_person_id", "visit_number"]
            #foreign_keys = ["jdc_person_id"]

        #convert and format the table schema dictionary
        tbl_schema_dict = convert_table_schema_df_to_dict(
            tbl_schema_df,
            table_description=schema_description,
            primary_keys=primary_keys,
            foreign_keys=foreign_keys,
        )
        tbl_schema_dict["description"] = schema_description
        validate_report = validate_schema(tbl_schema_dict)

        #write table schema dictionary to YAML file
        yaml_dir = os.path.join('schemas', f"{schema_path}.yaml")
        if validate_report.metadata_valid:
            with open(yaml_dir, "w") as f:
                yaml.safe_dump(tbl_schema_dict, f)
        else:
            print("Schema not valid due to these errors:")
            print("\n".join(validate_report["errors"]))
            sys.exit()


        json_dir = os.path.join('schemas', f"{schema_path}.json")
        if validate_report.metadata_valid:
            with open(json_dir, "w") as f:
                json.dump(tbl_schema_dict, f,indent=4)
        else:
            print("Schema not valid due to these errors:")
            print("\n".join(validate_report["errors"]))
            sys.exit()