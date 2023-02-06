import streamlit as st 
import sys
sys.path.append("pages")

st.set_page_config(
    page_title="Justice Community Opioid Intervention Network (JCOIN) Core Measures",
)

intro = """
Welcome to the JCOIN Core measure page. 
Here, you will find data dictionaries (i.e., table schemas) defining 
each of the Core Measure data tables.
"""
st.write(intro)