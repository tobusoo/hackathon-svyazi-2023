# _Hackathon 2023_
## About
This project was implemented within the framework of the All-Russian communications hackathon 2023 in ~ 2-3 days. Our team got the first place in our case. 

Team members:
- [tobuso](https://github.com/tobusoo)
- [dmitryukvyacheslav](https://github.com/dmitryukvyacheslav)
- [RomanMeringueTie](https://github.com/RomanMeringueTie)
- [WolfishTone](https://github.com/WolfishTone)
- [Mokujinnn](https://github.com/Mokujinnn)

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
Change the value of environment variables in the [.env](https://github.com/tobusoo/hackathon-svyazi-2023/blob/master/.env) file:
```
VK_APP_ID=YOUR_VK_APP_ID
VK_APP_SECRET=YOUR_VK_APP_SECRET
DADATA_SECRET=YOUR_DADATA_SECRET
TELEGRAM_API_ID=YOUR_TELEGRAM_API_ID 
TELEGRAM_API_HASH=YOUR_TELEGRAM_API_HASH
```

To get the Telegram api_id and api_hash, go to the "[API Development Tools]" section and fill out the form.

To get the DADATA_SECRET, login in [Dadata] and get token.

To get the VK_APP_SECRET and VK_APP_ID, login in [VK for development] and get tokens.

### Run
Starting the server...
```
python __init__.py
```
In another terminal, launch the website...
```
cd quasar-project
npm run dev
```
Open the browser at http://localhost:9000/#/

### Example
#### Main page
![image](https://github.com/tobusoo/hackathon-svyazi-2023/assets/106862439/d60ffa3a-74ed-46fa-96d0-c5d9b7eaf8b8)
#### Authorization page
![image](https://github.com/tobusoo/hackathon-svyazi-2023/assets/106862439/cc455022-967f-4589-8181-16ea394ca66b)
#### VK page
![image](https://github.com/tobusoo/hackathon-svyazi-2023/assets/106862439/55abf0bd-7bc9-45df-a8fb-ba031579a894)
#### Reverse geocoding page
![image](https://github.com/tobusoo/hackathon-svyazi-2023/assets/106862439/0842d90a-4023-4432-8e3f-5baeaf041ddd)
#### Telegram page
![image](https://github.com/tobusoo/hackathon-svyazi-2023/assets/106862439/e044d603-9d77-4d51-b3c7-f9082b80b671)


[VK for development]: <https://dev.vk.com/ru>
[Dadata]: <https://dadata.ru/api/>
[API Development Tools]: <https://my.telegram.org/apps>
