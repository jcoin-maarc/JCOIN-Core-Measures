from st_aggrid  import AgGrid,GridOptionsBuilder
import streamlit as st 
import pandas as pd 
from pathlib import Path
from frictionless import Schema
from collections.abc import MutableSequence
import io
#with a container/tab
REPO_DIR = "https://raw.githubusercontent.com/jcoin-maarc/JCOIN-Core-Measures/master"

def make_agrid(url_or_path):
    sourcedf = pd.read_csv(url_or_path)
    options = GridOptionsBuilder.from_dataframe(sourcedf)
    options.configure_side_bar()
    options.configure_selection(selection_mode = 'multiple')
    selected_table = AgGrid(
        sourcedf,
        gridOptions=options.build()
    )
    return selected_table

def render_schema_page(schema_name):
    st.write(f"{REPO_DIR}/schemas/{schema_name}.json")
    schema = Schema(f"{REPO_DIR}/schemas/{schema_name}.json").to_dict()
    
    for propname,prop in schema.items():
        st.markdown(f"## {propname}")
        if propname=="fields":
            selected_table = make_agrid(f"{REPO_DIR}/csvs/{schema_name}.csv")
        elif isinstance(prop,MutableSequence):
            st.markdown("\n".join([f"- {val}" for val in prop]))
        else:
            st.markdown(prop)

    schema['fields'] = selected_table 

    return schema


def download_excel(dictionary):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer,engine="xlsxwriter") as writer:
        for name,item in dictionary.items():
            try:
                df = pd.DataFrame(item)
            except ValueError:
                df = pd.DataFrame([item])

            df.to_excel(writer,sheet_name=name)
        writer.save()
    
    return buffer

def makepage(schema_name):
    schema = render_schema_page(schema_name)
    buffer = download_excel(schema)
    st.download_button(f"Download **{schema_name}** data dictionary",
        data=buffer,file_name=f"{schema_name}.xlsx")
    