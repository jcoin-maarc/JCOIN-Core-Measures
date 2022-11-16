import json 
from pathlib import Path 


schemapath = Path(__file__).parent.joinpath('schemas').glob("*")

for s in schemapath:
    with open(s,'r') as f:
        sjson = json.load(f)

    sjson['fields'] = [{k:v for k,v in f.items() if k!='encoding' and v} 
        for f in sjson['fields']]

    
    with open(s,'w') as f:
        json.dump(sjson,f,indent=4)
