import json
from pathlib import Path
from collections.abc import MutableMapping
import petl as etl

# dictionary utilities
def flatten_except_if(dictionary, parent_key=False, sep=".",except_keys=[]):
    """
    Turn a nested dictionary into a flattened dictionary. Taken from gen3 
    mds.agg_mds.adapter.flatten
    but added except keys and fixed a bug where parent is always False in MutableMapping

    :param dictionary: The dictionary to flatten
    :param parent_key: The string to prepend to dictionary's keys
    :param sep: The string used to separate flattened keys
    :param except_keys: keys to not flatten. Note, can be nested if using notation specified in sep
    :return: A flattened dictionary
    """

    items = []
    for key, value in dictionary.items():
        new_key = str(parent_key) + sep + key if parent_key else key
        if isinstance(value,MutableMapping) and not new_key in except_keys:
            items.extend(flatten_except_if(value, new_key, sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


class JsonToCsv:

    def __init__(self,jsonpath):
        self.dictionary = json.loads(Path(jsonpath).read_text(encoding="utf-8"))['fields']
        self.to_table()
    
    def to_table(self):
        flattened_dictionary = [flatten_except_if(field) for field in self.dictionary]
        table = ( 
            etl.fromdicts(flattened_dictionary)
            .convertall(lambda v: "|".join([str(_v) for _v in v]) if isinstance(v,list) else v)
        )
        self.table = table

    def tocsv(self,csvpath):
        self.table.tocsv(csvpath)

        return self



        
