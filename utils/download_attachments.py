import requests
import os
from datetime import datetime
from dateutil.parser import parse

def download_attachment(attachment, save_directory):
    # Descarga el archivo adjunto y lo guarda en la carpeta especificada
    url = attachment["url"]
    filename = attachment["filename"]
    save_path = os.path.join(save_directory, filename)

    response = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(response.content)

def download_attachments(messages, attachments_folder, channel_name):
    if not messages:
        return

    # Crear la carpeta de archivos adjuntos si no existe
    if not os.path.exists(attachments_folder):
        os.makedirs(attachments_folder)

    # Descargar archivos adjuntos
    for message in messages:
        if "attachments" in message:
            timestamp = message["timestamp"]
            dt = parse(timestamp)  # Usar parse() en lugar de fromisoformat()
            subfolder = dt.strftime("%Y-%m-%d_%H-%M")
            message_attachments_folder = os.path.join(attachments_folder, subfolder)

            for attachment in message["attachments"]:
                url = attachment["url"]
                filename = attachment["filename"]

                response = requests.get(url)

                # Crear la subcarpeta si no existe
                if not os.path.exists(message_attachments_folder):
                    os.makedirs(message_attachments_folder)

                # Guardar el archivo adjunto en la subcarpeta
                with open(os.path.join(message_attachments_folder, filename), "wb") as f:
                    f.write(response.content)
