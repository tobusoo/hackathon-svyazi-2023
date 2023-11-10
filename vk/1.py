import vk_api
from config import *

# https://oauth.vk.com/authorize? // запрос на получение access token
# client_id=51789951
# &display=page
# &redirect_url=https://oauth.vk.com/blank.html
# &scope=offline,friends,wall,status,docs,groups
# &response_type=token
# &v=5.21

if __name__ == "__main__":
    session = vk_api.VkApi(token=token)
    userStatus = session.method("status.get", {"user_id": 546543569})
    print(userStatus)