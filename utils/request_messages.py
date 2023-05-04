import requests

API_BASE_URL = "https://discord.com/api/v10/channels"


def get_messages(channel_id, authorization, limit=100, num_requests=5):
    headers = {
        "authorization": authorization,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    }

    all_messages = []
    last_message_id = None

    for _ in range(num_requests):
        url = f"{API_BASE_URL}/{channel_id}/messages?limit={limit}"
        if last_message_id:
            url += f"&before={last_message_id}"
        
        response = requests.get(url, headers=headers)
        messages = response.json()

        if not messages or "message" in messages:  # Comprueba si hay errores o no hay más mensajes
            break

        all_messages.extend(messages)
        last_message_id = messages[-1]["id"]

    return all_messages
