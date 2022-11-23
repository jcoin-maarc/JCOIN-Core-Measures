""" 
uses healdata utils tools to 
convert from json to csv
"""

from healdata_utils.transforms.csvtemplate.conversion import *
import sys
jsons = Path(__file__).parents[1].joinpath('schemas').glob("*")
csvs = Path(__file__).parents[1].joinpath('csvs').glob("*")

def to_csv():
    #convert json to csv
    for path in jsons:
        path = Path(path)
        outdir = path.parent.with_stem("csvs")
        fields = convert_json_to_template_csv(jsontemplate_path=path,fields_name='fields')
        etl.fromdicts(fields).tocsv(
            outdir/path.with_suffix(".csv").name,encoding='utf-8'
        )


def update_json():
    """ 
    update a json schema with fields and properties from csv file
    """
    
    #convert csv to json
    for path in csvs:
        path = Path(path)
        outfile = path.parent.with_stem("schemas")/path.with_suffix(".json").name
        schema = Schema(outfile)
        del schema['fields']
        fields = convert_template_csv_to_json(path,data_dictionary_props={})
        schema['fields'] = fields['data_dictionary']
        schema.to_json(outfile)

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
    elif sys.argv[1]=='updatejson':
        update_json()