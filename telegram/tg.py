import json
import os
import getpass
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetFullChannelRequest
from qrcode.main import QRCode
from config import *

# chat_name = 1001698136879 # it's chat
chat_name = 'sndkgram' # it's channel
# user = 1166414189 # find user
user = 0 # all users

qr = QRCode()


def gen_qr(token: str):
    qr.clear()
    qr.add_data(token)
    qr.print_ascii()


def display_url_as_qr(url: str):
    print(url)
    gen_qr(url)


async def get_messages_by_channel_name(client: TelegramClient, name, limit: int, search: str = '', find_by_user_id: int = 0):
    if not os.path.exists(str(name)):
        os.mkdir(str(name))

    messages_data = []
    count = 0
    channel_count = 0
    channel_about = None

    is_chat = None
    try:
        await client.download_profile_photo(name, f'{name}/profile.png')
        ch = await client.get_entity(name)
        ch_full = await client(GetFullChannelRequest(channel=ch))
        channel_about = ch_full.full_chat.about 
        channel_count = ch_full.full_chat.participants_count
    except ValueError:
        await client.download_profile_photo(-name, f'{name}/profile.png')
        is_chat = True


    async for message in client.iter_messages(name, search=search):
        if count == limit:
            break
        if not message.text:
            continue
        if len(message.text) == 0:
            continue
        
        user_id = None
        if message.from_id:
            user_id = message.from_id.user_id
        if find_by_user_id and user_id != find_by_user_id:
            continue

        # await client.download_media(message, f'{name}/{message.id}.png')

        reactions = []
        if message.reactions:
            for i in message.reactions.results:
                reactions.append({'emoticon': i.reaction.emoticon, 'count': i.count})
        
        url = None
        if not is_chat: 
            url = f'https://t.me/{name}/{message.id}'


        user_url = None
        if user_id:
            user_url = f'https://web.telegram.org/a/#{user_id}'

        data = {'date': str(message.date), 'text': message.text,
                'views': message.views, 'message_id': message.id,  
                'from_id': user_id, 'user_url': user_url,
                'message_url': url, 'reactions': reactions,}
        
        messages_data.append(data)
        count += 1
    
    json_data = {'subscribers': channel_count, 'about': channel_about,
                'messages_count':count, 'messages' : messages_data}
    return json_data


def write_json(filename: str, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


async def log_in_by_qr_code(client: TelegramClient):
    qr_login = await client.qr_login()

    r = False
    while not r:
        try:
            display_url_as_qr(qr_login.url)
            r = await qr_login.wait(30)
        except SessionPasswordNeededError:
            NotTntered = False
            while not NotTntered:
                password = getpass.getpass(prompt='Please enter your password: ')
                try:
                    NotTntered = await client.sign_in(password=password)
                    if (NotTntered):
                        r = True
                except:
                    pass
        except AttributeError:
            r = True
            break
        except:
            await qr_login.recreate()


async def log_in_by_phone(client: TelegramClient):
    await client.start() # type: ignore


async def main(client: TelegramClient):
    if (not client.is_connected()):
        await client.connect()
    await client.connect()

    await log_in_by_phone(client)
    # await log_in_by_qr_code(client)
    print('connected')

    try:
        data = await get_messages_by_channel_name(client, chat_name, limit=10, find_by_user_id=user)
        write_json(f'{chat_name}/{chat_name}.json', data)
        print(f'Parsed: {chat_name}')
    except UsernameInvalidError as e:
        print(e)

    client.disconnect()


if __name__ == '__main__':
    client = TelegramClient('session_name', API_ID, API_HASH)
    client.loop.run_until_complete(main(client))
