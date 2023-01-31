""" 
uses healdata utils tools to 
convert from json to csv to searchable dictionaries in html
"""

import healdata_utils.transforms.csvtemplate.conversion as healdata
import sys
import pandas as pd
from pathlib import Path
import click
import re

jsons = Path(__file__).parents[1].joinpath("schemas").glob("*")
csvs = Path(__file__).parents[1].joinpath("csvs").glob("*")


@click.command(name="tocsv")
def to_csv():
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

@click.command(name="tostreamlit")
def to_streamlit():
    def _to_html_list(v):
        items = v.split("|")
        ul = "<ul>{li}</ul>"
        list_items = ["<li>" + i + "</li>" for i in items]
        return ul.format(li="".join(list_items))

    for csvpath,jsonpath in zip(list(csvs),list(jsons)):
        schema = Schema(jsonpath)
        #TODO: get fields directly from schema above
        #TODO: contribute to Schema.to_summary method in frictionless
        fieldsdf = (
            pd.read_csv(csvpath)
            .applymap(
                lambda v: _to_html_list(v)
                if type(v) == str and re.search("\|", str(v))
                else v
            )
            # .fillna("")

            # .rename(columns={tmpcols[0]: "section"})
            # .pipe(
            #     lambda df: df.to_html(
            #         csvpath.parents[1]
            #         / "docs/assets"
            #         / csvpath.with_suffix(".html").name,
            #         columns=df.columns,
            #         escape=False,
            #         index=False,
            #     )
            # )
        )
        # make dataframe w



@click.group()
def cli():
    pass

cli.add_command(to_streamlit)
cli.add_command(update_json)
cli.add_command(to_csv)

if __name__ == "__main__":
    cli()
