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

def groupInfo(session, groupId):
    return session.method("groups.getById", {"group_id": groupId, "fields" : "activity,ban_info,can_post,can_see_all_posts,city,\
                                             contacts,counters,country,cover,description,finish_date,fixed_post,links,market,members_count,\
                                             place,site,start_date,status,verified,wiki_page"})

def usersInfo(session, userIds):
    return session.method("users.get", {"user_ids": userIds, "fields": "activities,about,blacklisted,blacklisted_by_me,books,\
                                        bdate,can_be_invited_group,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,\
                                        can_write_private_message,career,common_count,connections,contacts,city,country,crop_photo,\
                                        domain,education,exports,followers_count,friend_status,has_photo,has_mobile,home_town,photo_100,\
                                        photo_200,photo_200_orig,photo_400_orig,photo_50,sex,site,schools,screen_name,status,verified,\
                                        games,interests,is_favorite,is_friend,is_hidden_from_feed,last_seen,maiden_name,military,\
                                        movies,music,nickname,occupation,online,personal,photo_id,photo_max,photo_max_orig,quotes,\
                                        relation,relatives,timezone,tv,universities"})

def writeJson(info, filename):
    with open(filename, 'w', encoding='utf8') as file:
        for i in info:
            json.dump(i, file, separators=(',', ':'), indent=4, ensure_ascii=False)
            file.write("\n")



if __name__ == "__main__":
    session = vk_api.VkApi(token=token)

    info = groupInfo(session, 215278139)
    writeJson(info, "215278139.json")

    lst = "freshentree9,v.dmkrt,tobuso"
    
    info = usersInfo(session, lst)
    writeJson(info, "users.json")

