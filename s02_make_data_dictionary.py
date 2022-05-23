'''
Creates a human readable tabular data data dictionary 
Goal here is to create said data dictionary directly from 
the table schemas used. 

'''
import yaml
import pandas as pd
from jsonpath_ng import parse 
from pathlib import Path
dd_key = {
    "Category/Core Measure Section":"jcoin:core_measure_section",
    "Variable Name":"name",	
    "Variable Title":"title",	
    "Variable Description":"description",	
    "Variable Type":"type",
    "Required":"required",
    "Subsection Question Text (if applicable)":"jcoin:core_measure_subsection_text",
    "Question (if applicable)":"jcoin:core_measure_question",	
    "Max Length (if string type)":"maxLength",
    "Regular Expression pattern (see examples)":"pattern",	
    "Minimum (if integer/number)":"minimum",	
    "Possible Values":"enum",	
    "Example Values":"examples",	
    "Notes":"notes"
}

#open yaml
yaml_files = [
    "schemas/table-schema-baseline.yaml",
    "schemas/table-schema-time-points.yaml"
]


def make_dd_from_yaml(yaml_file):
    dd_values = []
    with open(yaml_file,'r') as f:
        schema = yaml.safe_load(f)
        for field in schema['fields']:
            dd_field = {}
            for name,exp in dd_key.items():
                parse_exp = parse(f"$..['{exp}']")
                value = parse_exp.find(field)
                if value:
                    dd_field[name] = value[0].value
            dd_values.append(dd_field)
    return dd_values



df = pd.DataFrame(make_dd_from_yaml(yaml_files[0]))

with pd.ExcelWriter('data_dictionaries/jcoin_core_measure_data_dictionaries.xlsx') as writer:
    for f in yaml_files:
        file_path = (
            Path(f).name
            .split(".")[0]
            .replace('table-schema','data-dictionary')
        )

        sheet_name = Path(f).stem

        dd = pd.DataFrame(make_dd_from_yaml(f))
        subsection = dd['Variable Name'].str.extract('(^[a-z][1-9]{1,2})')[0]
        dd.insert(2,'Core Measure Subsection',subsection)
        dd.to_csv('data_dictionaries/'+file_path+".tsv",sep='\t')
        dd.to_excel(
            writer,
            sheet_name=sheet_name,
        )

        # merge cells
        # cols_merge = [
        #     'Category/Core Measure Section',
        #     'Subsection Question Text (if applicable)',


        # ]






