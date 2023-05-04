# Discord Downloader

Discord Downloader is a Python script to download messages and attachments from Discord channels using the Discord API. It saves the messages in an Excel file and attachments in a folder structure with the channel name and date.

## Features

- Download messages from multiple Discord channels
- Save messages to an Excel file with separate sheets for each channel
- Download attachments from messages and save them in a structured folder hierarchy
- Customize the channels and settings through easy-to-edit configuration files

## Folder Structure
```
discord_downloader/
│
├── config/
│ ├── init.py
│ └── settings.py
│
├── utils/
│ ├── init.py
│ ├── data_processing.py
│ ├── download_attachments.py
│ └── request_messages.py
│
├── data/
│ ├── channels_url.txt
│ ├── channels_url_attachments.txt
│ └── attachments/ (folder to save downloaded attachments)
│
├── output/
│ └── Excel files with downloaded messages
│
├── main.py
├── main_attachments.py
├── requirements.txt
└── .gitignore
```

## Installation

1. Clone this repository or download it as a ZIP file.

2. Install Python 3.6 or later.

3. Install the required packages using the following command:

```
pip install -r requirements.txt
```


4. Obtain your Discord authorization token and add it to the `config/settings.py` file.

5. Create the folder data and add the channel URLs and names to the `data/channels_url.txt` and `data/channels_url_attachments.txt` files.
    Example `data/channels_url.txt` and `data/channels_url_attachments.txt` files:
    
    ```channel_name https://discord.com/channels/*space id*/*channel id*```

## Usage

1. To download messages and save them in an Excel file, run the following command:

```
python main.py
```

The Excel file will be saved in the `output` folder with the channel name and date.

2. To download attachments from a single channel, run the following command:

```
python main_attachments.py
```

The attachments will be saved in the `data/attachments` folder with the channel name, date, and time.

## Contributors
This project was developed by:
* [Raúl Sanz](https://github.com/rsanzd) - https://github.com/rsanzd
