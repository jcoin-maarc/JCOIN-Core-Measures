""" 
uses healdata utils tools to 
convert from json to csv to interactive dictionaries in a multipage streamlit app
"""

import os
import pandas as pd
from pathlib import Path
import click
import re
import petl as etl
from core_measures.utils import combine_schemas_to_excel,json_to_df,CsvToJson
from frictionless import Schema

jsons = list(Path(__file__).parents[1].joinpath("schemas").glob("*"))
csvs = list(Path(__file__).parents[1].joinpath("csvs").glob("*"))

def to_csv():
   
    for path in jsons:
        df = json_to_df(path)
        outdir = path.parent.with_stem("csvs")
        df.to_csv(outdir / path.with_suffix(".csv").name,index=False)

    # create excel
    xlsxpath = Path(outdir.with_name("xlsx"))
    xlsxpath.mkdir(exist_ok=True)
    combine_schemas_to_excel(csvs,str(xlsxpath/"core_measures.xlsx"))
    combine_schemas_to_excel(csvs,str(xlsxpath/"core_measures_long.xlsx"),separate_sheets=False)

def update_json():

    # convert csv to json
    for path in csvs:
        csvpath = path
        schemapath = path.parent.with_stem("schemas") / path.with_suffix(".json").name
        assert schemapath.exists(), f"Please make sure {schemapath.name} exists."
        CsvToJson(csvpath).to_json(schemapath)
    
    # run tocsv to make sure all files encoded properly and xlsx file updated
    to_csv()

# click commands
@click.group()
def cli():
    pass

tocsv_help = """
Flattens the json spec to a csv using the healdata_utils tool
"""

@click.command(name="tocsv",help=tocsv_help)
def clito_csv():
    to_csv()

update_json_help = """
update a json schema with fields and properties from csv file
"""
@click.command(name="updatejson",help=update_json_help)
def cliupdate_json():
    update_json()

cli.add_command(cliupdate_json)
cli.add_command(clito_csv)

if __name__ == "__main__":
    cli()
