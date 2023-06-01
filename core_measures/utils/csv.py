import json
from pathlib import Path
from collections.abc import MutableMapping
import petl as etl
#TODO: change CsvToJson just to function
def parse_dictionary_str(string,item_sep,keyval_sep):
    """ 
    parses a stringified dictionary into a dictionary
    based on item separator 

    """
    stritems = string.strip().split(item_sep)
    items = {}
    for stritem in stritems:
        item = stritem.split(keyval_sep,1)
        items[item[0]] = item[1].strip()
    
    return items 


def parse_list_str(string,list_sep="|"):
    if string:
        return string.strip().split(list_sep)



def convert_rec_to_json(field):
    ''' 
    converts a flattened dictionary to a nested dictionary
    based on JSON path dot notation indicating nesting
    '''
    field_json = {}
    for prop_path,prop in field.items():
        if prop:
            # initiate the prop to be added with the entire
            # field 
            prop_json = field_json
            # get the inner most dictionary item of the jsonpath
            nested_names = prop_path.split('.')
            for i,prop_name in enumerate(nested_names):
                is_last_nested = i+1==len(nested_names)
                if prop_json.get(prop_name) and not is_last_nested:
                    prop_json = prop_json[prop_name]
                # if no object currently 
                elif not is_last_nested:
                    prop_json[prop_name] = {}
                    prop_json = prop_json[prop_name]
                #assign property to inner most item
                else:
                    prop_json[prop_name] = prop

    return field_json


class CsvToJson:

    def __init__(self,csvpath):
        self.table = etl.fromcsv(csvpath,encoding="utf-8")

        self.to_dict()

    def csv_to_dict(self):

        cols = etl.fieldnames(self.table) 
        listcols = ['constraints.enum','trueValues','falseValues','missingValues']   
        intcols = ['constraints.maxLength','constraints.minLength','constraints.minimum','constraints.maximum',]
        boolcols = ['constraints.required','constraints.unique']
        
        convertlists = {name:parse_list_str for name in listcols if name in cols}
        convertints = {name:int for name in intcols if name in cols}
        convertbools = {name:bool for name in boolcols if name in cols}
        
        fields = (
            self.table
            .convert(convertlists)
            .convert(convertbools)
            .convert(convertints)
            .dicts()
        )
        self.fields = [convert_rec_to_json(field) for field in fields]
    def to_json(self,jsonpath):

        if Path(jsonpath).exists():
            with open(jsonpath,'r',encoding="utf-8") as f:
                schema = json.load(f)
                del schema['fields']
                schema['fields'] = self.fields

        ordered = {}
        for propname in ['name','title','description','fields']:
            if propname in schema:
                ordered[propname] = schema.pop(propname)
        ordered.update(schema)
        self.schema = ordered
        with open(jsonpath,'w') as f:
            json.dump(ordered,f,indent=4)

