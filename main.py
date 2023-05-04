import os
from datetime import datetime
from config.settings import AUTHORIZATION
from utils.data_processing import json_to_dataframe, save_dataframe_to_excel
from utils.download_attachments import download_attachment
from utils.request_messages import get_messages

# Punto de control 1: Inicio del programa
print("Iniciando el programa...")

# Pregunta al usuario si desea descargar los archivos adjuntos
download_attachments_choice = input("¿Desea descargar los archivos adjuntos? (Sí/No): ").lower()

# Lee las URLs de los canales y sus títulos desde el archivo channels_url.txt
with open("data/channels_url.txt", "r") as f:
    channels_data = [line.strip().split("\t") for line in f.readlines()]

dataframes = []
sheet_names = []

# Obtiene la fecha actual para crear las subcarpetas
current_date = datetime.now().strftime("%Y-%m-%d")

# Crea la subcarpeta 'output/current_date' si no existe
output_path = os.path.join("output", current_date)
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Procesa cada URL del canal y su título
for channel_title, url in channels_data:
    channel_id = url.split("/")[-1]

    # Punto de control 2: Descargando mensajes del canal
    print(f"Descargando mensajes del canal {channel_title}...")

    messages = get_messages(channel_id, AUTHORIZATION)
    df = json_to_dataframe(messages)
    dataframes.append(df)
    sheet_names.append(channel_title)

    # Descarga archivos adjuntos si el usuario eligió hacerlo
    if download_attachments_choice == "sí" or download_attachments_choice == "si":
        # Punto de control 3: Descargando archivos adjuntos
        print("Descargando archivos adjuntos...")

        # Crea la subcarpeta 'data/attachments/current_date/channel_title' si no existe
        attachments_path = os.path.join("data", "attachments", current_date, channel_title)
        if not os.path.exists(attachments_path):
            os.makedirs(attachments_path)

        for message in messages:
            for attachment in message["attachments"]:
                download_attachment(attachment, attachments_path)

# Punto de control 4: Guardando los mensajes en un archivo de Excel
print("Guardando los mensajes en un archivo de Excel...")

save_dataframe_to_excel(dataframes, sheet_names, os.path.join(output_path, "discord_messages.xlsx"))

# Punto de control 5: Finalización del programa
print("El programa ha finalizado con éxito.")
