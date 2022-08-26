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

#%% USER DEFINED INPUTS
#consistency codes
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
# USER DEFINED PATHS
schema_path = Path(__file__).parent/'schemas'/'table-schema-baseline.json'
data_path = r'C:\Users\kranz-michael\projects\jcoin-chestnut\tmp\frictionless\data\baseline.csv'
output_path = data_path.replace('.csv','{}')

#%% functions
def filter_consistency_codes(encodings):
    ''' 
    currently mapping consistency codes across
    all variables so filtering out individual
    (8/23: most are filtered but still manual work needed)
    '''

    return {
        key: val for key, val in encodings.items()
        if (not str(key) in consistency_codes.values()
         and not str(val) in consistency_codes.keys())
    }


def flip_dict(dictionary):
    ''' 
    this function flips values and keys in 
    a dictionary.
    ''' 
    return dict(zip(dictionary.values(),
                    dictionary.keys()))

def flip_encodings(encodings):
    ''' 
    Flip encodings for each variable name of a given encoding
    object.

    For example, after 
    encodings are mapped, they then need to 
    be flipped
    '''
    return {
    name: flip_dict(enc)
    for name, enc in encodings.items()
}

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
        for name in df
        if not pd.api.types.is_numeric_dtype(df[name])
    }
    df.replace(codes_if_string,inplace=True)

    # replace NaNs of missing cols
    # TODO: replace hardcoding with param
    missing_int_code = -4
    df.fillna(missing_int_code,inplace=True)

    return df

#%% DATA AND METADATA EXTRACTED FROM SOURCE
# read in metadata (load frictionless table schema)
with open(schema_path) as f:
    schema = json.load(f)

# get value lbls and check to ensure value is not in consistency codes
encodings = {
    f['name']: filter_consistency_codes(f['encoding']) 
    for f in schema['fields']
    if f.get('encoding')
}
# column_labels
# NOTE: should have title for every variable so no filtering
column_labels = {f['name']: f['title'] for f in schema['fields']}

#read in the data and map encodings and consistency codes
data = pd.read_csv(data_path)\
    .replace(encodings)\
    .pipe(map_consistency_codes,consistency_codes)\
    .convert_dtypes()

#%% Stata
# missing values must be one character between a-z
stata_codes = string.ascii_lowercase
stata_consistency_codes = {
        int(item[0]):stata_codes[i]
        for i,item in enumerate(consistency_codes.items())
}
stata_missing = {
    
    name:list(stata_consistency_codes.values()) 
    for name in data
    if pd.api.types.is_numeric_dtype(data[name])

}
stata_data = data.copy() 
for col in stata_data:
    if pd.api.types.is_numeric_dtype(stata_data[col]):
        stata_data[col] = stata_data[col].astype(float)

stata_data.replace({
    i:stata_consistency_codes 
    for i,var in stata_data.iteritems()
    if pd.api.types.is_numeric_dtype(var)
},inplace=True)

stata_encodings = flip_encodings(value_labels) # after  encodings are mapped, flip 
for name,encoding in stata_encodings.items():
    encoding.update(dict(zip(stata_consistency_codes.values(),consistency_codes.values())))

pyreadstat.write_dta(
    df=data.pipe(map_consistency_codes,stata_consistency_codes),
    column_labels=column_labels,
    variable_value_labels=stata_encodings,
    # missing_user_values=stata_missing,
    dst_path=output_path.format('.dta')

)

#%% SAS
sas_codes = string.ascii_uppercase
sas_consistency_codes = {
        int(item[0]):sas_codes[i]
        for i,item in enumerate(consistency_codes.items())
}
sas_encodings = flip_encodings(value_labels) # after  encodings are mapped, flip 
for name,encoding in sas_encodings.items():
    encoding.update(dict(zip(sas_consistency_codes.values(),consistency_codes.values())))
pyreadstat.write_xport(
    dst_path=output_path.format('xpt')
)
#%% SPSS
spss_data = data 
spss_consistency_codes = consistency_codes
spss_encodings = flip_encodings(encodings)
for name,encoding in sas_encodings.items():
    encoding.update(dict(zip(spss_consistency_codes.values(),consistency_codes.values())))

# SPSS takes numerics as missing values but only allows 3 per variable so making
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