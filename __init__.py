
from os import abort
from flask import Flask, jsonify, redirect, request, abort
from flask_cors import CORS
import vk_api
import requests
from vk.main import getUsersInfo
import json
from dotenv import load_dotenv
import os
load_dotenv()

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
app = Flask(__name__)
# enable CORS
CORS(app)

app.config.from_object(__name__)



# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/getPort', methods=['GET'])
def get_port():
    return (str(port_number))

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


@app.route('/api/vk/getMe', methods=['GET'])
def getme():
    if (vk_session):
        return (json.dumps({"me": "true"}))
    else:
        return (json.dumps({"me": "false"}))


@app.route('/api/vk/getUser', methods=['GET'])
def getuser():
    global vk_session
    if (vk_session == None):
        return abort(403)
    print(vk_session)
    return (vk_session.get(f"{VK_BASE_URL}/users.get",
    params={
        "user_ids": request.args.get("userID"),
        "v" : "5.154"
    }).text)
    
if __name__ == '__main__':
    app_kwargs = {}
    if FRONTEND_URL == "/":
        app_kwargs = dict(
            static_url_path='', 
            static_folder='quasar-project/dist')
    app.run(host='localhost', port=port_number, **app_kwargs)

