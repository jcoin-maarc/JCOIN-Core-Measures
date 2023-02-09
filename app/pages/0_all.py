import streamlit as st 
from core_measures.app import REPO_DIR

def load_csvs():
    schema_list = ['staff-baseline','baseline','time-points','staff-time-points']
    url_temp = REPO_DIR+"csvs/table-schema-{schema_name}.csv"
    return {
        schema_name:pd.read_csv(url_temp.format(schema=schema_name)) 
        for schema_name in schema_list
    }


def download_excel():
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer,engine="xlsxwriter") as writer:
        for name,item in load_csvs().items():
            try:
                df = pd.DataFrame(item)
            except ValueError:
                df = pd.DataFrame([item])

            df.to_excel(writer,sheet_name=name)

            # Get the workbook and the first worksheet
            worksheet = writer.sheets[name]

            # Freeze the headers (first row)
            worksheet.freeze_panes = 'A2'

            # Wrap header text
            for row in worksheet.iter_rows(min_row=1, max_col=worksheet.max_column, max_row=1):
                for cell in row:
                    cell.alignment = cell.alignment.copy(wrap_text=True)
        
        writer.save()
    
    return buffer

st.download_button(f"Click here to download all core measure data dictionaries",
    data=download_excel(),
    file_name="core-measure-fields.xlsx")