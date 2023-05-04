import os
from datetime import datetime
from config.settings import AUTHORIZATION
from utils.request_messages import get_messages
from utils.download_attachments import download_attachments

DATA_FOLDER = "data"
ATTACHMENTS_FOLDER = "attachments"
CHANNELS_URL_ATTACHMENTS_FILE = "channels_url_attachments.txt"

today = datetime.now().strftime("%Y-%m-%d")

# Leemos el archivo channels_url_attachments.txt
with open(os.path.join(DATA_FOLDER, CHANNELS_URL_ATTACHMENTS_FILE), "r") as f:
    channel_list = [line.strip().split("\t") for line in f.readlines()]

total_channels = len(channel_list)
for i, (channel_name, channel_url) in enumerate(channel_list, 1):
    print(f"Procesando canal {i}/{total_channels}: {channel_name}")
    
    # Extraemos el ID del canal de la URL
    channel_id = channel_url.split("/")[-1]

    # Obtenemos los mensajes del canal
    print(f"Obteniendo mensajes del canal {channel_name}...")
    messages = get_messages(channel_id, AUTHORIZATION)
    print(f"Se obtuvieron {len(messages)} mensajes del canal {channel_name}")

    # Descargamos los archivos adjuntos de los mensajes
    print(f"Descargando archivos adjuntos del canal {channel_name}...")
    download_attachments(
        messages,
        os.path.join(DATA_FOLDER, ATTACHMENTS_FOLDER, today, channel_name),
        channel_name,
    )
    print(f"Archivos adjuntos del canal {channel_name} descargados.\n")
