import streamlit as st 
import requests
from pathlib import Path
import time
import pandas as pd
import io 
import sys
import json
from collections.abc import MutableSequence

st.set_page_config(layout="wide")
SCHEMA_DIR = "https://api.github.com/repos/jcoin-maarc/JCOIN-Core-Measures/contents/schemas"
study_name = "JCOIN Core Measure"
fields_propnames = ["fields","data_dictionary"]
current_date = time.strftime("%Y_%m_%d")
## Read in schemas
read_schema_dir = lambda schema_dir_url: requests.get(schema_dir_url).json()
schemas = [json.loads(requests.get(schema["download_url"]).content) for schema in read_schema_dir(SCHEMA_DIR)]
## Download button of all schemas

# st.download_button(f"Click here to download all {study_name} data dictionaries",
#     data=io.BytesIO(excel),
#     file_name=Path(excel_url).stem+"_"+current_date+".xlsx")

## Toggle the type of schema
fields_toggle_type = "table"

## Select schema by title
schemas_title_keyed = {schema["title"]:schema["fields"] for schema in schemas}
selected = st.radio("Select a data dictionary:",options=schemas_title_keyed.keys())
schema = schemas_title_keyed[selected]
### download button
## download button depending on toggle type
# st.download_button(f"Download {schema_name}",data=buffer,file_name=f"{schema_name}.xlsx")

orderedschema = {}
for prop in ["title","description"]: #items to go first
    if prop in list(schema):
        orderedschema[prop] = schema.pop(prop)
orderedschema.update(schema)

field_tbl = pd.json_normalize(orderedschema[field_propname])
selected_columns = st.multiselect(options=field_tbl.columns)
if fields_toggle_type=="table":
    orderedschema[field_propname] = field_tbl[selected_columns]
elif fields_toggle_type=="json records":
    fields = orderedschema[field_propname] = field_tbl[selected_columns].to_dict(orient="records")
else:
    raise Exception("only json and tabular toggle types")

st.markdown(f"# {study_name}")

st.download_button(f"Download Selected Fields from {selected} in csv",data=fields.to_csv(index=False).encode('utf-8'),file_name=f"{schema_name}.csv")
st.download_button(f"Download Selected Fields {selected} in json",data=orderedschema,file_name=f"{schema_name}.json")

# st.download_button(f"Click here to download all {study_name} data dictionaries",
#     data=io.BytesIO(excel),
#     file_name=Path(excel_url).stem+"_"+current_date+".xlsx")
for propname,prop in orderedschema.items():

    st.markdown(f"## {propname}")

    if isinstance(prop,MutableSequence):
        st.markdown("\n".join([f"- {val}" for val in prop]))
    else:
        st.write(prop)


def download_excel(dictionary):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer,engine="xlsxwriter") as writer:
        for name,item in dictionary.items():
            try:
                df = pd.DataFrame(item)
            except ValueError:
                df = pd.DataFrame([item])

            df.to_excel(writer,sheet_name=name)
    
    return buffer

def makepage(schema_name):
    fieldsdf = load_csv(f"{REPO_DIR}/csvs/{schema_name}.csv")
    schema = load_schema(schema_name)
    schema['fields'] = fieldsdf
    buffer = download_excel(schema)

    st.download_button(f"Download {schema_name} in json",data=Schema(f"{REPO_DIR}/schemas/{schema_name}.json").to_json(),file_name=f"{schema_name}.xlsx")
    schema = render_schema_page(fieldsdf=fieldsdf,schema=schema,schema_name=schema_name)
