""" 
uses healdata utils tools to 
convert from json to csv to interactive dictionaries in a multipage streamlit app
"""

import os
import pandas as pd
from pathlib import Path
import click
import re
import petl as etl
from core_measures.utils import combine_schemas_to_excel,json_to_df
from frictionless import Schema

jsons = list(Path(__file__).parents[1].joinpath("schemas").glob("*.json"))
csvs = list(Path(__file__).parents[1].joinpath("csvs").glob("*.csv"))

def to_csv():
   
    for path in jsons:
        df = json_to_df(path)
        outdir = path.parent.with_stem("csvs")
        df.to_csv(outdir / path.with_suffix(".csv").name,index=False)



def to_excel():
    xlsxpath = Path(csvs[0].parent.with_name("xlsx"))
    xlsxpath.mkdir(exist_ok=True)
    combine_schemas_to_excel(csvs,str(xlsxpath/"core_measures.xlsx"))
    combine_schemas_to_excel(csvs,str(xlsxpath/"core_measures_long.xlsx"),separate_sheets=False)
