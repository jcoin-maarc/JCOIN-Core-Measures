""" 
uses healdata utils tools to 
convert from json to csv to interactive dictionaries in a multipage streamlit app
"""

import sys
import pandas as pd
from pathlib import Path
import click
import re

jsons = Path(__file__).parents[1].joinpath("schemas").glob("*")
csvs = Path(__file__).parents[1].joinpath("csvs").glob("*")


@click.command(name="tocsv")
def to_csv():
    import healdata_utils.transforms.csvtemplate.conversion as healdata
    # convert json to csv
    for path in jsons:
        path = Path(path)
        outdir = path.parent.with_stem("csvs")
        fields = healdata.convert_json_to_template_csv(
            jsontemplate_path=path, fields_name="fields"
        )
        etl.fromdicts(fields.data).tocsv(
            outdir / path.with_suffix(".csv").name, encoding="utf-8"
        )


@click.command(name="updatejson")
def update_json():
    """
    update a json schema with fields and properties from csv file
    """
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

streamlit_app_template = """ 
import utils

utils.makepage("{schema_name}")

""" 

@click.command(name="tostreamlit")
def to_streamlit():
    """ 
    creates a page for each schema in the multipage streamlit app
    NOTE: this command assumes all packages called from saved script are set up to run correctly
    """
    for i,csvpath in enumerate(sorted(csvs)):
        schema_name = csvpath.stem
        pagesdir = Path(__file__).parents[1]/"app"/"pages"
        pagespath = pagesdir.joinpath(f"{str(i+1)}_{schema_name}.py")
        pagescript = streamlit_app_template.format(schema_name=schema_name)
        pagespath.write_text(pagescript)





@click.group()
def cli():
    pass

cli.add_command(to_streamlit)
cli.add_command(update_json)
cli.add_command(to_csv)

if __name__ == "__main__":
    cli()
