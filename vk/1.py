import vk_api
import json
from config import *

# https://oauth.vk.com/authorize? // запрос на получение access token
# client_id=51789951
# &display=page
# &redirect_url=https://oauth.vk.com/blank.html
# &scope=offline,friends,wall,status,docs,groups
# &response_type=token
# &v=5.21

def groupInfo(session ,groupId):
    return session.method("groups.getById", {"group_id": groupId, "fields" : "activity,ban_info,can_post,can_see_all_posts,city,\
                                             contacts,counters,country,cover,description,finish_date,fixed_post,links,market,members_count,\
                                             place,site,start_date,status,verified,wiki_page"})

def writeJson(info, filename):
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(info[0], file, separators=(',', ':'), indent=4, ensure_ascii=False)

if __name__ == "__main__":
    session = vk_api.VkApi(token=token)
    
    info = groupInfo(session, 215278139)
    writeJson(info, "215278139.json")

