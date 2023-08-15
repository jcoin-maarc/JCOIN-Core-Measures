import json 
from pathlib import Path 
from healdata_utils.transforms.frictionless.conversion import convert_frictionless_tableschema
from healdata_utils.validators.validate import validate_vlmd_csv,validate_vlmd_json

schemas = list(Path("schemas").glob("*.json"))


for path in schemas:
    schema = json.loads(path.read_text())
    for prop in ["missingValues","primaryKey"]:
        del schema[prop]
    
    for field in schema["fields"]:
        del field["original_name"]

    
    dds = convert_frictionless_tableschema(schema)
    csvreport = validate_vlmd_csv(dds["templatecsv"])
    jsonreport = validate_vlmd_json(dds["templatejson"])

    if csvreport["valid"] and jsonreport["valid"]:
        Path("heal").joinpath(path.name).write_text(json.dumps(schema,indent=2))
    else:
        raise Exception(f"{str(path.name)} was not converted into a valid HEAL VLMD DD")