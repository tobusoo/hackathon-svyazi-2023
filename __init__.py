
from os import abort
#from flask import Flask, jsonify, redirect, request, abort
#from flask_cors import CORS
from quart import Quart, request, redirect, abort
from quart_cors import cors, route_cors
import requests
import json
from dotenv import load_dotenv
from tg.tg import get_messages_by_channel_name

from telethon import TelegramClient, errors
import os

import telethon

# DADATA
from dadata import Dadata
from geo.geo import *

load_dotenv()
client = TelegramClient(session='anon2', api_id=int(os.environ['TELEGRAM_API_ID']), api_hash=os.environ['TELEGRAM_API_HASH'])

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
app = cors(app, allow_headers=["Authorization"])

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
    print(userid)
    if (not userid.isnumeric()):
        if (userid.find(".com/") != -1):
            userid=userid[userid.find(".com/")+len(".com/"):]
        print(userid)
        userid = vk_session.get(url='https://api.vk.com/method/utils.resolveScreenName?v=5.131',
                                params = { "screen_name": userid}).json()
        userid = userid['response']['object_id']
    resp = vk_session.get('https://api.vk.com/method/users.get?v=5.131',
                   params={'user_ids' : userid,
                           'fields' : 'bdate, photo_200, status'}).json()
    print(resp)
    return(resp)

@app.route('/api/vk/getGroups', methods=['GET'])
def vk_get_groups():
    if (vk_session == None):
        return abort(403)
    groupid = str(request.args.get('groupid'))
    print(groupid)
    if (not groupid.isnumeric()):
        if (groupid.find(".com/") != -1):
            groupid=groupid[groupid.find(".com/")+len(".com/"):]
        print(groupid)
        groupid = vk_session.get(url='https://api.vk.com/method/utils.resolveScreenName?v=5.131',
                                params = { "screen_name": groupid }).json()
        print(groupid)
        groupid = groupid['response']['object_id']
    resp = vk_session.get('https://api.vk.com/method/groups.getById?v=5.131',
                   params={'group_id' : groupid,
                           'fields' : 'members_count, name, screen_name, photo_200, status'}).json()
    print(resp)
    return(resp)

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

    return_data = {'postals': postals, 'adresses': adresses}
    return return_data

@app.route('/api/telegram/getMessages', methods=['GET'])
async def tg_getm():
    name = str(request.args.get('channel_name'))
    search = str(request.args.get('search'))
    userID = str(request.args.get('userid'))
    # print(name, search, userID)
    # return {}

    global client
    await client.connect()
    limit=100
    msgs = await get_messages_by_channel_name(client=client, 
                                         search=search,
                                         name=name,     #название канала     
                                         find_by_user_id=userID,
                                         limit=limit)
    await client.disconnect()

    return(msgs)

                            
    
   
    

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

