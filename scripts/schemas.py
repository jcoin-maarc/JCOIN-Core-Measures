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
jsons = Path(__file__).parents[1].joinpath('schemas').glob("*")
csvs = Path(__file__).parents[1].joinpath('csvs').glob("*")

@click.command(name="tocsv")
def to_csv():
    #convert json to csv
    for path in jsons:
        path = Path(path)
        outdir = path.parent.with_stem("csvs")
        fields = healdata.convert_json_to_template_csv(jsontemplate_path=path,fields_name='fields')
        etl.fromdicts(fields.data).tocsv(
            outdir/path.with_suffix(".csv").name,encoding='utf-8'
        )

@click.command(name="updatejson")
def update_json():
    """ 
    update a json schema with fields and properties from csv file
    """
    
    #convert csv to json
    for path in csvs:
        path = Path(path)
        outfile = path.parent.with_stem("schemas")/path.with_suffix(".json").name
        assert outfile.exists(),f"Please make sure {outfile.name} exists."
        schema = Schema(outfile)

        fields = healdata.convert_template_csv_to_json(path,data_dictionary_props={})

        if schema.get('fields'):
            del schema['fields']

        schema['fields'] = fields['data_dictionary']
        schema.to_json(outfile)

@click.command(name="tohtml")
@click.option("--freeze-fields",default=['name','title'])
@click.option("--freeze-headers",is_flag=True,default=True)
def to_html(freeze_fields,freeze_headers):
    def _to_html_list(v):
        items = v.split("|")
        ul = "<ul>{li}</ul>"
        list_items = ["<li>"+i+"</li>" for i in items]
        return ul.format(li="".join(list_items))
    def _add_searchbar():
        pass

    def _freeze_headers(styledf):
        if freeze_headers:
            print("Freezing headers")
            styledf = styledf.set_sticky(axis=1)
        return styledf
    
    for csvpath in csvs:
        df = pd.read_csv(csvpath)
        dfhtml = (
            df
            .set_index(freeze_fields)
            .applymap(lambda v:_to_html_list(v) 
                if type(v)==str and re.search("\|",str(v)) else v)
            .fillna("")
            .style.set_sticky(axis=0)
            .pipe(_freeze_headers)
        )
        dfhtml.to_html(
            csvpath.parents[1]/
            'docs/assets'/
            csvpath.with_suffix(".html").name)

@click.group()
def cli():
    pass 

cli.add_command(to_html)
cli.add_command(update_json)
cli.add_command(to_csv)

if __name__=="__main__":
    cli()