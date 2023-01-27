""" 
uses healdata utils tools to 
convert from json to csv to searchable dictionaries in html
"""

import healdata_utils.transforms.csvtemplate.conversion as healdata
import sys
import pandas as pd
from pathlib import Path
import click
import re

jsons = Path(__file__).parents[1].joinpath("schemas").glob("*")
csvs = Path(__file__).parents[1].joinpath("csvs").glob("*")


@click.command(name="tocsv")
def to_csv():
    # convert json to csv
    for path in jsons:
        path = Path(path)
        outdir = path.parent.with_stem("csvs")
        fields = healdata.convert_json_to_template_csv(
            jsontemplate_path=path, fields_name="fields"
        )
        etl.fromdicts(fields.data).tocsv(
            outdir / path.with_suffix(".csv").name, encoding="utf-8"
        )


@click.command(name="updatejson")
def update_json():
    """
    update a json schema with fields and properties from csv file
    """

    # convert csv to json
    for path in csvs:
        path = Path(path)
        outfile = path.parent.with_stem("schemas") / path.with_suffix(".json").name
        assert outfile.exists(), f"Please make sure {outfile.name} exists."
        schema = Schema(outfile)

        fields = healdata.convert_template_csv_to_json(path, data_dictionary_props={})

        if schema.get("fields"):
            del schema["fields"]

        schema["fields"] = fields["data_dictionary"]
        schema.to_json(outfile)


# html_template = """
# <html>

# <head>
#     <script>
#     {filterTable}
#     {selectColumns}
#     </script>
# </head>
# <body>

# </body>
# """


@click.command(name="tohtml")
@click.option(
    "--freeze-fields", default=["custom.jcoin:core_measure_section", "name", "title"]
)
@click.option("--freeze-headers", is_flag=True, default=True)
def to_html(freeze_fields, freeze_headers):
    def _to_html_list(v):
        items = v.split("|")
        ul = "<ul>{li}</ul>"
        list_items = ["<li>" + i + "</li>" for i in items]
        return ul.format(li="".join(list_items))

    # def _filter_table(colnum,colname):

    #     filterCol = Path(__file__).joinpath('filterTable.js').read_text()
    #     filterColInput = """<input type="text" id="filterInput" onkeyup="filterTable({colnum})" placeholder="Filter by {colname}">"""

    #     return filterColInput

    # def _col_checkbox(colnum,colname):

    #     selectColumn = Path(__file__).joinpath('selectTable.js').read_text()
    #     selectTableInput = f"""{colname}<br><input type="checkbox" name="columnCheckbox" value={colnum} onchange="updateTable()" checked>{colname}<br>"""

    #     return selectTableInput

    def _freeze_headers(styledf):
        pass

    # filterTable = Path(__file__).joinpath('filterTable.js').read_text()
    # selectColumn = Path(__file__).joinpath('selectTable.js').read_text()

    for csvpath in csvs:
        df = pd.read_csv(csvpath)
        # df.columns = [_col_with_searchbar(colnum, colname) for enumerate(df.columns)]

        tmpcols = [
            "custom.jcoin:core_measure_section",
            "name",
            "title",
            "description",
            "constraints.enum",
            "type",
            "format",
            "trueValues",
            "falseValues",
        ]

        dfhtml = (
            df.applymap(
                lambda v: _to_html_list(v)
                if type(v) == str and re.search("\|", str(v))
                else v
            )
            .fillna("")
            # TODO: include all columns and have ability to hide/unhide rows
            [tmpcols]
            .rename(columns={tmpcols[0]: "section"})
            .pipe(
                lambda df: df.to_html(
                    csvpath.parents[1]
                    / "docs/assets"
                    / csvpath.with_suffix(".html").name,
                    columns=df.columns,
                    escape=False,
                    index=False,
                )
            )
        )


@click.group()
def cli():
    pass


cli.add_command(to_html)
cli.add_command(update_json)
cli.add_command(to_csv)

if __name__ == "__main__":
    cli()
