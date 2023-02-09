import streamlit as st 
import sys
sys.path.append("pages")


st.set_page_config(
    page_title="Justice Community Opioid Intervention Network (JCOIN) Core Measures",
    layout="wide",
    initial_sidebar_state='collapsed'
)

intro = """
Welcome to the JCOIN Core measure page. 
Here, you will find data dictionaries (i.e., table schemas) defining 
each of the Core Measure data tables. To download all data dictionaries in 
one excel file, click button below:
"""
st.write(intro)


