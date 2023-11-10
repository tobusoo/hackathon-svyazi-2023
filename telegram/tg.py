import json
from telethon import TelegramClient

api_id = 20343413
api_hash = '5ac3d169381320ca0befa82dd98400b1'

chat_name = 'sndkgram'


def get_messages_by_channel_name(client: TelegramClient, name: str, limit: int):
    messages_data = []
    messages = client.iter_messages(name, limit)
    count = 0

    for message in messages:
        if len(message.text) == 0:
            continue

        data = {'date': str(message.date), 'text': message.text, 'views': message.views}
        messages_data.append(data)
        count += 1
    
    json_data = {'count':count, 'messages' : messages_data}
    return json_data


def write_json(filename: str, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    data = get_messages_by_channel_name(client, chat_name, 50)
    write_json(f'tg_{chat_name}.json', data)

    client.disconnect()

if __name__ == '__main__':
    main()