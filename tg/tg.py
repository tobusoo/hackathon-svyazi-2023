import os
import sys
import json
import getpass
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetFullChannelRequest


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
                'messages_count':count, 'messages' : messages_data, 'profile_photo_path': f'{name}/profile.png'}
    return json_data


def write_json(filename: str, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


async def main(client: TelegramClient):
    if (not client.is_connected()):
        await client.connect()
    await client.connect()

    phone = str(input('Enter your phone number: ')) # Your number
    code = str(None)
    await client.sign_in(phone)
    try:
        code = str(input('Enter code: '))
        await client.sign_in(phone, code)
    except SessionPasswordNeededError:
        password = getpass.getpass('Enter your password: ')
        await client.sign_in(phone, password=password)

    # chat_name = 1001698136879 # it's chat
    chat_name = 'sndkgram' # it's channel
    # user = 1166414189 # find user
    user = 0 # all users

    print('connected')
    try:
        data = await get_messages_by_channel_name(client, chat_name, limit=10, find_by_user_id=user)
        write_json(f'{chat_name}/{chat_name}.json', data)
        print(f'Parsed: {chat_name}')
    except UsernameInvalidError as e:
        print(e)

    client.disconnect()


if __name__ == '__main__':
    extDataDir = os.getcwd()
    if getattr(sys, 'frozen', False):
        extDataDir = sys._MEIPASS
    load_dotenv(dotenv_path=os.path.join(extDataDir, '.env'))

    TELEGRAM_API_ID = os.environ.get('TELEGRAM_API_ID')
    TELEGRAM_API_HASH = os.environ.get('TELEGRAM_API_HASH')
    print(TELEGRAM_API_ID)
    client = TelegramClient('anon', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    client.loop.run_until_complete(main(client))
