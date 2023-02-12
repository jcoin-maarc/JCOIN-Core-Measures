import streamlit as st 
import requests
from core_measures.app.utils import REPO_DIR,make_agrid
from pathlib import Path
import time

url = f"{REPO_DIR}/xlsx/core_measures.xlsx"
url_long = f"{REPO_DIR}/xlsx/core_measures_long.xlsx"
excel = requests.get(url).content
excel_long = requests.get(url_long).content
current_date = time.strftime("%Y_%m_%d")

st.download_button(f"Click here to download all core measure data dictionaries",
    data=excel,
    file_name=Path(url).name+"_"+current_date)

df = pd.read_csv(excel_long)
make_agrid(df)
