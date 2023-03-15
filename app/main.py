import streamlit as st 
import requests
from core_measures.app.utils import REPO_DIR,make_agrid
from core_measures import app
from pathlib import Path
import time
import pandas as pd
import io 
import sys

st.set_page_config(layout="wide")
lbls = {
    'all':"All",    
    'table-schema-baseline': 'Clients: Baseline',
    'table-schema-time-points': 'Clients: Timepoints',
    'table-schema-staff-baseline': 'Staff: Baseline',
    'table-schema-staff-time-points': 'Staff: Timepoints'}


intro = """
Welcome to the JCOIN Core measure search tool! 
Here, you will find data dictionaries (i.e., table schemas) defining 
each of the JCOIN Core Measure data tables and associated properties.

"""
st.write(intro)


url = f"{REPO_DIR}/xlsx/core_measures.xlsx"
url_long = f"{REPO_DIR}/xlsx/core_measures_long.xlsx"
excel = requests.get(url).content
current_date = time.strftime("%Y_%m_%d")

st.download_button(f"Click here to download all core measure data dictionaries",
    data=excel,
    file_name=Path(url).stem+"_"+current_date+".xlsx")

tab0,tab1,tab2,tab3,tab4 = st.tabs(lbls.values())

alltbl = lbls.pop("all")
allhelp = """ 
- To search for all core measure variables (across clients and staff and datasets), use the search tool below.
    - `schema` = dataset
    - `name` = name of variable in analytic dataset
    - `custom.jcoin:original_variable_name` = name of variable in Source PDF
    - `constraints.enum` = Possible values

- Click other tabs data dictionaries for specific tables and corresponding table level properties (eg missingValues (ie reserve codes for missingness, table descriptions, primary keys))
""" 
with tab0:
    st.markdown(allhelp)
    excel_long = requests.get(url_long).content
    excel_file = pd.ExcelFile(io.BytesIO(excel_long))
    schemas = pd.read_excel(excel_file,sheet_name="schemas")
    redox_colnames = ["schema","custom.jcoin:core_measure_section","name","custom.jcoin:original_name","constraints.enum"]
    st.dataframe(schemas[redox_colnames])

print(lbls.keys)
for name,tab in zip(lbls.keys(),[tab1,tab2,tab3,tab4]):
    with tab:
        print(name)
        app.utils.makepage(name)