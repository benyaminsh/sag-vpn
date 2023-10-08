from pyrogram import Client, filters
from decouple import config
import requests
import re

token = config('TOKEN',default='9916efd144ea2cf77e9aa22ee08c50d45e4a62e2')
base_url = config('BASE_URL', default="http://127.0.0.1:8000")
api_id = config("API_ID", default=29966682, cast=int)
api_hash = config("API_HASH", default="c7cee45eb9a296b05c005c25febc6264")
servers_count = 0


app = Client("my_account", api_id=api_id, api_hash=api_hash)



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
    result = []
    for res in response:
        try:
            username = str(res['username'])
            result.append(username)
            # app.start()
            # app.join_chat(username[1:])
            # app.stop()
        except:
            pass

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


def get_status():
    message = f"""
Server Count : {servers_count}
Channels Count : {len(get_channels())}
Channels ID : 
""" + "\n".join(get_channels())

    return message



@app.on_message(filters.private)
async def find_command(client, message):
    if message.text in commands.keys():
        await message.reply(commands[message.text])

channels = [].extend(get_channels())

@app.on_message(filters.chat(chats=channels))
async def main(client, message):
    try:
        configs = find_config(message.text)
        for config in configs:
            send_to_server(config, message.sender_chat.username)
            global servers_count
            servers_count += 1
    except:
        pass




commands = {
    "ping": "Pong -!",
    "status": get_status(),
}

app.run()
