import pandas as pd

def json_to_dataframe(json_data):
    # Convierte los datos JSON en un DataFrame de pandas
    df = pd.DataFrame(json_data)
    return df

def save_dataframe_to_excel(dataframes, sheet_names, output_filename):
    # Guarda múltiples DataFrames en un archivo de Excel con diferentes hojas
    with pd.ExcelWriter(output_filename) as writer:
        for df, sheet_name in zip(dataframes, sheet_names):
            df.to_excel(writer, sheet_name=sheet_name)
