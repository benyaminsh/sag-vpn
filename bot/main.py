from pyrogram import Client, filters
from decouple import config
import requests
import re
import json

token = config('TOKEN',default='9916efd144ea2cf77e9aa22ee08c50d45e4a62e2')
base_url = config('BASE_URL', default="http://127.0.0.1:8000")
api_id = config("API_ID", default=29966682, cast=int)
api_hash = config("API_HASH", default="c7cee45eb9a296b05c005c25febc6264")
servers = []




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
        except:
            pass

    return result


def create_channel_in_server(channel):
    url = base_url + "/settings/create-channels/"

    payload = {'username': channel}

    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)




def find_config(text):
    patterns = [r"trojan://.*", r"vmess://.*", r"vless://.*",r"ss://.*"]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        if matches:
            return matches
        else:
            pass

    return False




@app.on_message(filters.private)
async def find_command(client, message):
    if message.text == 'status':
        try:
            jsonFile = open("servers.json", "r", encoding='utf-8')
            servers_count = len(json.loads(jsonFile.read()))
        except:
            servers_count = 0

        text = f"""
Server Count : {servers_count}
Channels Count : {len(get_channels())}
Channels ID :
""" + " - ".join(get_channels())
        await message.reply(text)

    elif message.text == 'ping':
        await message.reply('Pong')

    elif 'join' in message.text:
        try:
            url = "".join(str("".join(str(message.text).split('join'))).split('https://t.me/'))
            with app:
                await app.join_chat(url)
                await message.reply('joined')
                create_channel_in_server(url)
        except:
            await message.reply('Not Fund or Invalid')

    elif message.text == 'restart':
        for channel in get_channels():
            with app:
                try:
                    await app.join_chat(channel)
                    await message.reply(f"Join To : {channel}")
                except:
                    pass




@app.on_message(filters or filters.group)
async def main(client, message):
    try:
        configs = find_config(message.text)
        for config in configs:
            send_to_server(config, message.sender_chat.username)
            servers.append(config)
            jsonString = json.dumps(servers, ensure_ascii=False, indent=4)
            jsonFile = open("servers.json", "w", encoding='utf-8')
            jsonFile.write(jsonString)
            jsonFile.close()
    except:
        pass


app.run()

