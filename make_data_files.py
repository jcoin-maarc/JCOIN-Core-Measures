''' 
makes SAS, SPSS, and Stata
data files from frictionless package and associated data (csv)

TODO: make from the datapackage.json
TODO: incorporate into jdc-utils (potentially running validation first and then outputting different files)

From table schema JSONs: :
1. maps encodings to data and stores pyreadstat object
2. maps consistency codes and appends pyreadstat object
3. 
'''
import pyreadstat
from pathlib import Path
import json
import pandas as pd
import numpy as np
import string

def filter_consistency_codes(encodings):
    ''' 
    currently mapping consistency codes across
    all variables so filtering out individual
    (8/23: most are filtered but still manual work needed)
    '''

    return {
        key: val for key, val in encodings.items()
        if not str(key) in consistency_codes and not str(val) in consistency_codes
    }


def flip_encoding(encoding):
    return dict(zip(encoding.values(),
                    encoding.keys()))

def map_consistency_codes(df,codes):
    ''' 
    Maps consistency codes to data.
    First, map already decoded consistency codes (i.e., string vars)
    Second, fill missing values (ie NaN) with Missing int code

    TODO: embed specific consistency codes for each variable?
    NOTE: currently, mapping consistency codes if variable is not numeric
    TODO: pull consistency codes directly from schema (need to add to schema )
    ---need to delete '' (first missingValue in schema) so first half are ints
     and 2nd are the corresponding string lbls
    '''
    df = df.copy() 

    # replace string cols with codes
    codes_if_string = {
        name: {
            val:key
            for key, val in codes.items()
        }
        for name in data
        if not pd.api.types.is_numeric_dtype(df[name])
    }
    df.replace(codes_if_string,inplace=True)

    #replace nans of string cols with Missing lbl
    codes_string_nans = {
        name:{np.nan:'Missing'}
        for name in codes_if_string
    }
    df.replace(codes_string_nans,inplace=True)

    # replace NaNs of missing cols
    # TODO: replace hardcoding with param
    missing_int_code = codes[-4]
    df.fillna(missing_int_code,inplace=True)

    return df

# USER DEFINED PATHS
schema_path = Path(__file__).parent/'schemas'/'table-schema-baseline.json'
data_path = r'C:\Users\kranz-michael\projects\jcoin-chestnut\tmp\frictionless\data\baseline.csv'
output_path = data_path.replace('.csv','{}')


consistency_codes = {
    # from Chestnut
    -3: 'NotAsked',
    -4: 'Missing',
    -6: 'Confidential',
    -7: 'Refused',
    -8: 'DontKnow',
    -9: 'LegitimatelySkipped',
    # from core measures for boolean columns
    -10: 'Refused to answer',
    -11: 'n/a not recently incarcerated',
    -12: "Don't recall",
    -13: "Don't Know",
    -14: 'Do not know',
    -98: 'Unknown'
    # TODO: from core measure other categorical columns

 }
stata_codes = string.ascii_lowercase
stata_consistency_codes = {
        int(item[0]):stata_codes[i]
        for i,item in enumerate(consistency_codes.items())
}
sas_codes = string.ascii_uppercase
sas_consistency_codes = {
        int(item[0]):sas_codes[i]
        for i,item in enumerate(consistency_codes.items())
}

# read in metadata (load frictionless table schema)
with open(schema_path) as f:
    schema = json.load(f)

# get value lbls and check to ensure value is not in consistency codes
value_labels = {
    f['name']: filter_consistency_codes(f['encoding']) for f in schema['fields']
    if f.get('encoding')
}
# column_labels
# NOTE: should have title for every variable so no filtering
column_labels = {f['name']: f['title'] for f in schema['fields']}

#read in the data and map encodings and consistency codes
data = pd.read_csv(data_path)\
    .replace(value_labels)\
    .pipe(map_consistency_codes,stata_consistency_codes)
# now that encodings are mapped, flip so key is value in data and value is label
flipped_value_labels = {
    name: flip_encoding(enc)
    for name, enc in value_labels.items()
}

# SPSS
#SPSS takes numerics as missing values but only allows 3 per variable so making
# for now going to not define missing values for SPSS files
# spss_missing = {name:list(map(int,consistency_codes.keys())) 
#         for name in data if pd.api.types.is_numeric_dtype(data[name])}
pyreadstat.write_sav(
    df=data,
    column_labels=column_labels,
    variable_value_labels=flipped_value_labels,
    dst_path=output_path.format('.sav'),
    # missing_ranges=spss_missing
)
# # SAS
# pyreadstat.write_xport(
#     **output_params,
#     dst_path=output_path.format('xpt')

# )
#Stata
# missing values must be one character between a-z 
stata_missing = {
    
    name:list(stata_consistency_codes.values()) 
    for name in data
    if pd.api.types.is_numeric_dtype(data[name])

}
#TODO: add missing value labels to each variable
pyreadstat.write_dta(
    df=data.pipe(map_consistency_codes,stata_consistency_codes),
    column_labels=column_labels,
    variable_value_labels=flipped_value_labels,
    missing_user_values=stata_missing,
    dst_path=output_path.format('.dta')

)
