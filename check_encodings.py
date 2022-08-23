""" 
check that encoding labels for a CSV 
submission are equivalent to the possible values (ie enum, true/falseValues)

"""
from pathlib import Path
import pandas as pd

file_name = "table-schema-time-points{}.csv"
csv_schema = Path(__file__).parent /"csvs"/file_name.format("")
# lbl_list = ["enum", "trueValues", "falseValues", "missingValues"]
lbl_list = ["enum", "trueValues", "falseValues"]

combine_list = lambda x: "|".join(x.loc[x.notna()])
strip_list = lambda x: "|".join([x.strip() for x in x.split('|')])
# current
current = pd.read_csv(
    csv_schema, index_col="name"
)[lbl_list]
current["lbls"] = current[lbl_list]\
    .apply(combine_list, axis="columns")\
    .map(strip_list)
# add
encodings = pd.read_csv(
    csv_schema, index_col="name"
)[["encoding"]]

check = current[["lbls"]].join(encodings, how="left")
check["lbls_from_encodings"] = check["encoding"]\
    .fillna('')\
    .str.replace("=(\d+|-\d+)", "", regex=True)\
    .map(strip_list)
    
check["is_same"] = check["lbls_from_encodings"].fillna("") == check["lbls"].fillna("")

check.to_csv('test.csv')

