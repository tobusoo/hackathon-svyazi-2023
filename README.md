# _Hackathon 2023_
## _Preparation_
Install requirements for server:
``` 
pip install -r requirements.txt
```
Install [node.js](https://nodejs.org/en) 
Install requirements for site:
``` 
cd quasar-project
npm install
npm install axios
``` 
Change the value of environment variables in the .env file:
```
VK_APP_ID=YOUR_VK_APP_ID
VK_APP_SECRET=YOUR_VK_APP_SECRET
DADATA_SECRET=YOUR_DADATA_SECRET
TELEGRAM_API_ID=YOUR_TELEGRAM_API_ID 
TELEGRAM_API_HASH=YOUR_TELEGRAM_API_HASH
```

To get the Telegram api_id and api_hash, go to the "[API Development Tools]" section and fill out the form

To get the DADATA_SECRET, login in [Dadata] and get token.

To get the VK_APP_SECRET and VK_APP_ID, login in [VK for development] and get tokens.

### Run
Starting the server
```
python __init__.py
```
In another terminal, launch the website
```
cd quasar-project
npm run dev
```

[VK for development]: <https://dev.vk.com/ru>
[Dadata]: <https://dadata.ru/api/>
[API Development Tools]: <https://my.telegram.org/apps>