import json 
from pathlib import Path 
from frictionless import Schema

def add_encodings(schema,encodings):
    schema = Schema(schema)
    encodings = Schema(encodings)

    for field in schema.fields:
        if encodings.get(field['name']):
            field.update(encodings[field['name']])

    return schema




schemapath = Path(__file__).parent.joinpath('schemas').glob("*")

for s in schemapath:
    with open(s,'r') as f:
        sjson = json.load(f)

    sjson['fields'] = [{k:v for k,v in f.items() if k!='encodings' and v} 
        for f in sjson['fields']]

    
    with open(s,'w') as f:
        json.dump(sjson,f,indent=4)
