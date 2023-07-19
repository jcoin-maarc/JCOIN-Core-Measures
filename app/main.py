import streamlit as st 
import requests
from pathlib import Path
import time
import pandas as pd
import io 
import sys
import json
import re
from collections.abc import MutableSequence

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

st.set_page_config(layout="wide")
SCHEMA_DIR = "https://api.github.com/repos/jcoin-maarc/JCOIN-Core-Measures/contents/schemas"
SCHEMA_DIR = str(Path(__file__).parents[1]/"schemas")
study_name = "JCOIN Core Measure"
fields_propnames = ["fields","data_dictionary"]
field_propname = "fields"
current_date = time.strftime("%Y_%m_%d")

# Study title 
st.markdown(f"# {study_name}")

## Read in schemas

# Via github api
# read_schema_dir = lambda schema_dir_url: requests.get(SCHEMA_DIR).json()
# schemas = [json.loads(requests.get(schema["download_url"]).content) for schema in read_schema_dir(SCHEMA_DIR)]

# Via local directory
read_schema_dir = lambda _ : list(Path(SCHEMA_DIR).glob("*"))
schemas = [json.loads(path.read_text()) for path in read_schema_dir()]

## Download button of all schemas in excel format
## TODO: compile from schemas json array
## TODO: make option of csvs with descriptor
## NOTE: for now just leaving as core meaures
excel_path = Path(re.sub("/schemas$","/xlsx",SCHEMA_DIR)).as_posix()
excel = xlsx_file = requests.get(requests.get(excel_path).json()[0]["download_url"]).content
st.download_button(f"Click here to download all {study_name} data dictionaries",
    data=io.BytesIO(excel),
    file_name="core_measures"+"_"+current_date+".xlsx")

## Select schema by title
selected = st.radio("Select a data dictionary:",options=[schema["title"] for schema in schemas])
for schema in schemas:
    if selected==schema["title"]:
        orderedschema = dict(schema)

## Toggle how fields are viewed and downloaded
field_tbl = pd.json_normalize(orderedschema[field_propname])
field_columns = field_tbl.columns.tolist()
selected_columns = st.multiselect(label="Selected Properties",options=field_columns,default=field_columns)
field_view_exts = {"table":".csv","json records":".json"}
fields_view_type = st.radio(label="Variable View Type",options=field_view_exts.keys())
if fields_view_type=="table":
    fields = orderedschema[field_propname] = field_tbl[selected_columns]
    download_fields = lambda fields: fields.to_csv(index=False).encode('utf-8')
    st_fields = lambda fields: st.dataframe(fields_tbl)
elif fields_view_type=="json records":
    fields = orderedschema[field_propname] = field_tbl[selected_columns].to_dict(orient="records")
    download_fields = lambda fields: json.dumps(orderedschema,indent=2)
    st_fields = lambda fields:st.json(fields)
else:
    raise Exception("only json and tabular toggle types")


# Download button for data dictionary
st.download_button(f"Download Selected Data Dictionary in {selected} format",
    data=download_fields(fields),
    file_name=f"{slugify(selected)}{field_view_exts[fields_view_type]}")


# render schema properties
for propname,prop in orderedschema.items():

    st.markdown(f"## {propname}")
    if propname==field_propname:
        st_fields()
    elif isinstance(prop,MutableSequence):
        st.markdown("\n".join([f"- {val}" for val in prop]))
    else:
        st.write(prop)