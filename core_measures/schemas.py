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
from core_measures.utils import combine_schemas_to_excel
from frictionless import Schema

jsons = list(Path(__file__).parents[1].joinpath("schemas").glob("*"))
csvs = list(Path(__file__).parents[1].joinpath("csvs").glob("*"))

def to_csv():
    import healdata_utils.transforms.csvtemplate.conversion as healdata
    # convert json to csv
    for path in jsons:
        path = Path(path)
        outdir = path.parent.with_stem("csvs")
        fields = healdata.convert_json_to_template_csv(
            jsontemplate_path=path, fields_name="fields"
        )
        fieldsdata = etl.fromdicts(fields.data)
        cols = [c for c in ['jcoin:core_measure_section','name','type','description','trueValues','falseValues',
            'constraints.enum'] if c in fieldsdata.header()]
        cols.extend([c for c in fieldsdata.header() if not c in cols])
        fieldsdata.cut(cols).tocsv(outdir / path.with_suffix(".csv").name, encoding="utf-8")

    xlsxpath = Path(outdir.with_name("xlsx"))
    xlsxpath.mkdir(exist_ok=True)
    combine_schemas_to_excel(csvs,str(xlsxpath/"core_measures.xlsx"))


def update_json():

    import healdata_utils.transforms.csvtemplate.conversion as healdata
    # convert csv to json
    for path in csvs:
        path = Path(path)
        outfile = path.parent.with_stem("schemas") / path.with_suffix(".json").name
        assert outfile.exists(), f"Please make sure {outfile.name} exists."
        schema = Schema(outfile)

        fields = healdata.convert_template_csv_to_json(path, data_dictionary_props={})

        if schema.get("fields"):
            del schema["fields"]

        schema["fields"] = fields["data_dictionary"]
        schema.to_json(outfile)
        # run tocsv to make sure all files encoded properly and xlsx file updated
        to_csv()

streamlit_app_template = """ 
from core_measures import app

app.utils.makepage("{schema_name}")

""" 
streamlit_help = """ 
creates a page for each schema in the multipage streamlit app
NOTE: this command assumes all packages called from saved script are set up to run correctly
"""
@click.command(name="tostreamlit",help=streamlit_help)
def to_streamlit():
    for i,csvpath in enumerate(sorted(csvs)):
        schema_name = csvpath.stem
        pagesdir = Path(os.getcwd())/"app"/"pages"
        pagespath = pagesdir.joinpath(f"{str(i+1)}_{schema_name}.py")
        pagescript = streamlit_app_template.format(schema_name=schema_name)
        pagespath.write_text(pagescript)

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


cli.add_command(to_streamlit)
cli.add_command(cliupdate_json)
cli.add_command(clito_csv)

if __name__ == "__main__":
    cli()
