""" 
uses healdata utils tools to 
convert from json to csv
"""

import healdata_utils.transforms.csvtemplate.conversion as healdata
import sys
import pandas as pd
from pathlib import Path
jsons = Path(__file__).parents[1].joinpath('schemas').glob("*")
csvs = Path(__file__).parents[1].joinpath('csvs').glob("*")
html = Path(__file__).parents[1].joinpath('htmls')
html.mkdir(exist_ok=True)
def to_csv():
    #convert json to csv
    for path in jsons:
        path = Path(path)
        outdir = path.parent.with_stem("csvs")
        fields = healdata.convert_json_to_template_csv(jsontemplate_path=path,fields_name='fields')
        etl.fromdicts(fields.data).tocsv(
            outdir/path.with_suffix(".csv").name,encoding='utf-8'
        )
# to_csv()
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

def to_html():
    to_html_list = lambda v: ['<li>+v1+</li>' for v1 in '|'.split(v)]
    for csvpath in csvs:
        df = pd.read_csv(csvpath)
        dfhtml = (
            df
            .set_index('name')
            .applymap(lambda v:[f"<ul>{to_html_list(v)}</ul>"] if type(v)==str else v)
            .fillna("")
            .style.format(escape='html')
            .to_html(
                csvpath.parents[1]/
                'htmls'/
                csvpath.with_suffix(".html").name)
        )

cli_message = '''
Please enter either tocsv or updatejson:
if updatejson, will take your csv file of fields and update the existing
json frictionless schema. If to csv, will take existing json frictionless schema
and produce and flattened tabular data dictionary in a csv file.
'''

if __name__=="__main__":
    
    assert sys.argv[1] in ['tocsv','updatejson'],cli_message

    if sys.argv[1]=='tocsv':
        to_csv()
        to_html()
    elif sys.argv[1]=='updatejson':
        update_json()
    elif sys.argv[1]=='tohtml':
        to_html()