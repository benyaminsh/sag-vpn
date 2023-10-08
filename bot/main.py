from pyrogram import Client, filters
from decouple import config
import requests
import re

token = config('TOKEN',default='9916efd144ea2cf77e9aa22ee08c50d45e4a62e2')
base_url = config('BASE_URL', default="http://127.0.0.1:8000")
api_id = config("API_ID", default=29966682, cast=int)
api_hash = config("API_HASH", default="c7cee45eb9a296b05c005c25febc6264")


def send_to_server(config, channel):
    url = base_url + "/servers/create-config/"

    payload = {
        'config': config,
        'channel': channel
    }

    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)


def get_channels():
    url = base_url + "/settings/get-channels/"

    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.request("GET", url, headers=headers).json()
    result = [res['username'] for res in response]
    return result


def find_config(text):
    patterns = [r"trojan://.*", r"vmess://.*", r"vless://.*"]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        if matches:
            return matches
        else:
            pass

    return False


channels_username = get_channels()

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.chat(chats=channels_username))
async def hello(client, message):
    try:
        configs = find_config(message.text)
        for config in configs:
            send_to_server(config, message.sender_chat.username)
    except:
        pass


app.run()
