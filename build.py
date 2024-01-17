""" 
script to generate jsonschema and frictionless schemas
 from yaml definitions
"""
import yaml
from pathlib import Path
import os
import re
import json
import copy
from collections.abc import MutableMapping, MutableSequence, MutableSet,Sequence
from functools import reduce

from core_measures import schemas as schema_utils

os.chdir(Path(__file__).parent)

# load yaml
def load_yaml(filepath):
    with open(filepath) as f:
        yamlfile = yaml.safe_load(f)

    return yamlfile

# load all yamls
def load_all_yamls(directory="schemas/dictionary"):
    filepaths = Path(directory).glob("*.yaml")
    return {filepath.stem: load_yaml(filepath) for filepath in filepaths}

def resolve_refs(items, schema, parentkey=False):
    """
    resolve pseudo-json references

    item is the item to be iterated through
    and schema is the overall schema to reference

    NOTE: these are pseudo as $ref is used simply for replacement of
    any value (ie $ref doesnt have to be )
    JSON references: https://datatracker.ietf.org/doc/html/draft-pbryan-zyp-json-ref-03
    """

    schema_resolved = {}
    for key, item in items.items():
        # resolve refs
        if key == "$ref":
            path = item.split("/")
            anchor = path.pop(0)
            if anchor == "#":
                get_item = lambda _item, key: _item.get(key, {})
                _resolved = reduce(get_item, path, schema)
                resolved = resolve_refs(_resolved, schema)
                schema_resolved.update(resolved)

        # resursively call and map to output schema
        elif isinstance(item, MutableMapping):
            schema_resolved[key] = resolve_refs(item, schema)
        elif isinstance(item, (MutableSequence, MutableSet)):
            resolveditem = []
            for val in item:
                if isinstance(val, MutableMapping):
                    _resolved = resolve_refs(val, schema)
                else:
                    _resolved = val
                resolveditem.append(_resolved)

            schema_resolved[key] = resolveditem
        else:
            schema_resolved[key] = item

    return schema_resolved

def run_pipeline_step(input, step):
    """function for input into the reduce functool
    function where the input is the instance and fxn is
    a tuple of either length 1 if only param is input
    and greater than eq 1 if there are additional paramters to fxn
    with dict of parameters second item in tuple
    """
    step = [_step for _step in step if _step]
    fxn = step[0]
    if len(step) > 1:
        params = step[1]
        return fxn(input, **params)
    elif len(step) == 1:
        return fxn(input)
    else:
        raise Exception("Step must be at least of length 1")

if __name__ == "__main__":
    # compile frictionless schema fields
    dictionary = load_all_yamls()

    # compile json schema fields
    json_pipeline = [
        # recursive fxn so need to grab items from overall dictionary for json paths
        (resolve_refs, {"schema": dictionary})
        
    ]
    tblschemas = resolve_refs(dictionary,dictionary)
    del tblschemas["_definitions"]

    for name,schema in tblschemas.items():
        Path(f"schemas/table-schema-{name}.json").write_text(json.dumps(schema, indent=4))

    schema_utils.to_csv()
    schema_utils.to_excel()