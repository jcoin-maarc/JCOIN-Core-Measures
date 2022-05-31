''' 
Generates documentation
based on the Table Schema and 
other metadata. 

Work in progress

Switched from html to markdown to support mkdocs

'''
from jsonpath_ng.jsonpath import Fields
from frictionless import Schema
from pathlib import Path 

SCHEMA_DIR = f'{Path(__file__).parent}/schemas'

title_template = '''
### {title}
'''
#title
def add_title(field):
    title = field.get('title',None)
    if title:
        return title_template.format(title=title.title())
    else:
        return ''

# def add_core_measure(field):
#     core_measure_exp = Fields("custom").child(Fields("jcoin:core_measure_id"))
#     core_measure = core_measure_exp.find(field)
#     if core_measure:
#         return  core_measure[0].value.capitalize()
#     else:
#         return  'Not in core measures'

#descriptions
def add_description(field):
    return field.get('description','NO DESCRIPTION')

#variable name
def add_variable_name(field):
    return field.get('name',"NO VARIABLE NAME")

#variable values
def add_enums(field):
    enum_exp = Fields("constraints").child(Fields("enum"))
    enum_list = enum_exp.find(field)
    if enum_list:
        # enum_list_html = [f"<li>{enum}</li>" for enum in enum_list]
        # enum_title = "<p><strong>Possible Values:</strong></p>"
        # return enum_title + f"<ul>{enum_list_html}</ul>"
        return ','.join(enum_list[0].value)
    else:
        return "Any of the fields type and other constraints"

def add_type(field):
    type_str = field.get('type','NO TYPE SPECIFIED')
    return type_str.title()

#note
def add_note(field):
    note_exp = Fields('custom').child(Fields('notes'))
    note = note_exp.find(field)
    if note:
        return note[0].value
    else:
        return ""

def add_examples(examples):
    return examples


def add_core_measure_question(field):
    question_exp = Fields('custom').child(Fields("jcoin:core_measure_question"))
    question = question_exp.find(field)

    subsection_exp = Fields('custom').child(Fields("jcoin:core_measure_subsection_text"))
    subsection = subsection_exp.find(field)
    
    if question and subsection:
        f'{subsection[0].value}\n{question[0].value}'
    if question:
        return question[0].value
    else:
        return ''

def add_required(field):
    req_exp = Fields("constraints").child(Fields('required'))
    req = req_exp.find(field)
    if req:
        return 'Yes' 
    else:
        return ''
#make an ordered dict of mappings
# field_md_template = ''' 

# --------------------------------------------
# {title}
#  |               |                          |
# ----------------- | --------------------------
# |**Variable name** | `{variable_name}`|
# |**JCOIN Core Measure Question Text** | {question} |
# |**Description:** | {description} |
# |**Variable type** | {type}|
# |**Possible values** | {enums}|
# '''
def make_field_md(field):
    # field_md = field_md_template.format(
    #     title=add_title(field),
    #     question=add_core_measure_question(field),
    #     core_measure=add_core_measure(field),
    #     description=add_description(field),
    #     variable_name=add_variable_name(field),
    #     enums=add_enums(field),
    #     type=add_type(field),
    # )

    field_list = [
        ("","\n---------"), #field divider
        ("",add_title(field)),
        ("**Variable name:**",f"```{add_variable_name(field)}```"),
       ("**JCOIN Core Measure Question Text:**", add_core_measure_question(field)),
        ("**Description:**",add_description(field)),
        ("**Variable type:**",add_type(field)),
        ("**Possible values:**",add_enums(field)),
        ("**Required:**",add_required(field)),
        ("**Notes:**",add_note(field))
    ]

    field_md = "\n\n".join([prop_name+" "+prop for prop_name,prop in field_list if prop])


    #field_expandable = f'<details>\n\t<summary>\n\t{field_md}\n</details>'

    
    return field_md

section_md_template = '''
----------
## **{section} Fields**
----------
'''
def get_section(field,first_level='custom',second_level='jcoin:core_measure_section'):
    json_section = Fields(first_level).child(Fields(second_level)).find(field)
    if json_section:
        section = json_section[0].value
    else:
        section = "Other"
    return section
    
baseline_schema_path = f'{SCHEMA_DIR}/table-schema-baseline.yaml'
timepoint_schema_path = f'{SCHEMA_DIR}/table-schema-time-points.yaml'
schemas = [Schema(baseline_schema_path),Schema(timepoint_schema_path)]


# Field Codebook
overall_md = '**Click on a section category to view variables!**\n\n'
for schema in schemas:
    field_md_list = []
    section = '' #initiate section name
    for field in schema.fields:
        #compare this section with last section and add section header to markdown if new
        if section!=get_section(field):
            collapse_start = f'\n<details>\n\t<summary><h2>{get_section(field)}</h2></summary>\n'
            collapse_end = '\n</details>\n'
            if section:
                field_md_list.append(collapse_end)

            field_md_list.append(f'{collapse_start}')
            #field_md_list.append(get_section(field))
        section = get_section(field)

        field_md_list.append(make_field_md(field))
    
    field_md_list.append('\n</details>\n')
    fields_mds = '\n'.join(field_md_list)

    #schema/dataset/file level 
    schema_description = schema.get('description','No description')
    schema_file_name = schema_description.split(":")[0].lower().replace(" ","_")
    overall_md+=f"\n# {schema_description}\n"
    overall_md+=fields_mds #add field markdowns to schema dataset/file level
with open(f"codebooks/codebook.md",'w',encoding='utf-8') as f:
    f.write(overall_md)


