
from os import abort
import re
from tkinter import W
#from flask import Flask, jsonify, redirect, request, abort
#from flask_cors import CORS
from quart import Quart, request, redirect, abort
from quart_cors import cors
import requests
import json
from dotenv import load_dotenv

from telethon import TelegramClient, errors
import os

import telethon

# DADATA
from dadata import Dadata
from geo.geo import *

load_dotenv()
client = TelegramClient(session='my_session', api_id=int(os.environ['TELEGRAM_API_ID']), api_hash=os.environ['TELEGRAM_API_HASH'])

if os.path.exists("./quasar-project/dist/index.html"):
    FRONTEND_URL = "/"
else:
    FRONTEND_URL = 'http://localhost:9000'
# configuration
port_number = 7000
vk_session = None

VK_BASE_URL = 'https://api.vk.com/method'
DEBUG = True

# instantiate the app
app = Quart(__name__)
# enable CORS
app = cors(app)

app.config.from_object(__name__)

@app.route('/api/vk/callback', methods=['GET'])
def save_session_key():
    global vk_session
    
    code = request.args.get('code')
    print(code)
    vk_auth = requests.get("https://oauth.vk.com/access_token", 
                 params = {"client_id" : os.environ['VK_APP_ID'],
                           "client_secret" : os.environ['VK_APP_SECRET'],
                            "redirect_uri" : "http://localhost:7000/api/vk/callback",
                            "code" : code}
    ).json()
    vk_session = requests.Session()
    vk_session.headers["Authorization"] = "Bearer " + vk_auth["access_token"]
    print(vk_session)
    # return("Key saved successfully")
    return redirect(FRONTEND_URL)

@app.route('/api/vk/getUsers', methods=['GET'])
def vk_get_users():
    if (vk_session == None):
        return abort(403)
    userid = str(request.args.get('userid'))
    if (not userid.isnumeric()):
        return vk_session.get('https://api.vk.com/method/users.get?v=5.131', params={'user_ids' : request.args.get('userid'), 'fields' : 'bdate, photo'}).json()
        
@app.route('/api/vk/getMe', methods=['GET'])
def getme():
    if (vk_session):
        return (json.dumps({"me": "true"}))
    else:
        return (json.dumps({"me": "false"}))

@app.route('/api/telegram/requestcode', methods=['GET'])
async def login_number():
    global client    
    await client.connect()
    print(str(request.args.get('phone')))
    pcode = await client.send_code_request(str(request.args.get('phone')))
    print(pcode)
    print(request.args.get('phone'))
    print(pcode.phone_code_hash)
    await client.disconnect()
    return({"result" : pcode.phone_code_hash})

@app.route('/api/telegram/signin', methods=['GET'])
async def tg_login():
    global client
    if (client == None):
        print('Abort')
        return (abort(400))
    
    await client.connect()
    print('In sign in')
    if (await client.get_me() != None ):
        res = await client.get_me()
        return (res.to_json())
    print('In sign in after')
    code = str(request.args.get('code'))
    print(code)
    password = str(request.args.get('password'))
    print(password)
    if (password == ""):
        res = await client.sign_in(code=code)
    else:
        try:
            res = await client.sign_in(code=code)
        except telethon.errors.SessionPasswordNeededError:
            res = await client.sign_in(password=password)
    await client.disconnect()
    return (res.to_json())
               
    
@app.route('/api/geo/search', methods=['GET'])
def geo_search():
    dadata = Dadata(os.environ['DADATA_SECRET'])
    radius = int(request.args.get('radius'))
    lat = float((request.args.get('lat')))
    lon = float((request.args.get('lon')))
    max_count = 20
    response = dadata_get_addresses(dadata, lat, lon, radius, max_count)
    adresses = addresses_to_json(response)
    
    unique_postal_ids = find_postal_ids(response)
    postals = postals_to_json(dadata, unique_postal_ids)

    info = {'adresses': adresses, 'postals': postals}

    return info
    


## @app.route('/api/telegram/login/code', methods=['GET'])

## @app.route('/api/telegram/login/2fa', methods=['GET'])

## @app.route('/api/telegram/getGroup', methods=['GET'])

if __name__ == '__main__':
    app_kwargs = {}
    if FRONTEND_URL == "/":
        app_kwargs = dict(
            static_url_path='', 
            static_folder='quasar-project/dist')
    app.run(host='localhost', port=port_number, **app_kwargs)

