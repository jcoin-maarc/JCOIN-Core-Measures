from st_aggrid  import AgGrid,GridOptionsBuilder
import streamlit as st 
import pandas as pd 
from pathlib import Path

# @st.experimental_memo
# def load_data():
#     pass 

#with a container/tab
repo_dir = Path(__file__).parents[1]
sourcedf = pd.read_csv(repo_dir.joinpath("csvs/table-schema-baseline.csv"))
sourcecols = sourcedf.columns.tolist()

sections_colname = 'custom.jcoin:core_measure_section'
sections_vals = sourcedf[sections_colname].fillna("None").unique()
# section selector
sections_select = st.multiselect(
    label="Select sections to look at:",
    options=sections_vals,
    default=sections_vals
)
#column selector
column_options = st.multiselect(
    label="Select variable info to look at:",
    options=sourcedf.columns.tolist(),
    default=['name','title','description','type'])


# search selector
column_to_search = st.selectbox("Select how you want to search for variables:",options=sourcecols)
# search text
text_to_search = st.text_input(f"Type your search in {column_to_search} here ")

#filter dataframe based on sections/columns
is_selected_section = sourcedf[sections_colname].isin(sections_select)
if text_to_search:
    contains_text = (
        sourcedf[column_to_search]
        .str.contains(pat=text_to_search,regex=False,case=False)
    )
    is_selected = (is_selected_section & contains_text)
else:
    is_selected = (is_selected_section & is_selected_section)
   
targetdf = sourcedf.loc[is_selected,column_options]
#render dataframe
#selected_rows = AgGrid(targetdf)

st.dataframe(targetdf)