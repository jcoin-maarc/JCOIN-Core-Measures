from st_aggrid  import AgGrid,GridOptionsBuilder
import streamlit as st 
import pandas as pd 
from pathlib import Path
from frictionless import Schema
from collections.abc import MutableSequence
import io
#with a container/tab
REPO_DIR = "https://raw.githubusercontent.com/jcoin-maarc/JCOIN-Core-Measures/master/"
schema_name ="table-schema-baseline"

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
    schema = Schema(f"{REPO_DIR}/schemas/{schema_name}.json")
    
    for propname,prop in schema.items():
        st.markdown(f"## {propname}")
        if propname=="fields":
            selected_table = make_agrid(f"{REPO_DIR}/csvs/{schema_name}.csv")
        elif isinstance(prop,MutableSequence):
            st.markdown("\n".join([f"- {val}" for val in prop]))
        else:
            st.markdown(prop)

    outdict = schema.to_dict()
    schema['fields'] = selected_table 

    return schema


def download_excel_button(dictionary):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer,engine="xlsxwriter") as writer:
        for name,item in dictionary.items():
            try:
                df = pd.DataFrame(item)
            except ValueError:
                df = pd.DataFrame([item])

            df.to_excel(writer,sheet_name=name)
        writer.save()

    st.download_button("Download selected data dictionary",
        buffer)



schema = render_schema_page(schema_name)
download_excel_button(schema)
