import pandas as pd

def convert_messages_to_dataframe(messages):
    data = []
    for message in messages:
        data.append({
            "id": message["id"],
            "content": message["content"],
            "timestamp": message["timestamp"],
            "author_id": message["author"]["id"],
            "author_username": message["author"]["username"],
            "attachments": message["attachments"]
        })

    df = pd.DataFrame(data)
    return df

def save_dataframes_to_xlsx(dataframes, sheet_names, output_file):
    writer = pd.ExcelWriter(output_file, engine="xlsxwriter")

    for df, sheet_name in zip(dataframes, sheet_names):
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
