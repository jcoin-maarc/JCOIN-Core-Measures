import streamlit as st 
import requests
from core_measures.app.utils import REPO_DIR,make_agrid
from pathlib import Path
import time
import pandas as pd
import io 


url = f"{REPO_DIR}/xlsx/core_measures.xlsx"
url_long = f"{REPO_DIR}/xlsx/core_measures_long.xlsx"
excel = requests.get(url).content
excel_long = requests.get(url_long).content
current_date = time.strftime("%Y_%m_%d")

st.download_button(f"Click here to download all core measure data dictionaries",
    data=excel,
    file_name=Path(url).name+"_"+current_date)

excel_file = pd.ExcelFile(io.BytesIO(excel_long))
readme = pd.read_excel(excel_file,sheet_name="README")
schemas = pd.read_excel(excel_file,sheet_name="schemas")

st.write(readme.iloc[:,1:])
make_agrid(schemas)
