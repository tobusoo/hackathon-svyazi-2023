import vk_api
import json
from config import *

# https://oauth.vk.com/authorize? // запрос на получение access token
# client_id=51789951               // Надо просто скопировать ссылку и вставить в браузер
# &display=page
# &redirect_url=https://oauth.vk.com/blank.html
# &scope=offline,friends,wall,status,docs,groups
# &response_type=token
# &v=5.21

def getGroupInfo(session: vk_api.VkApi, groupId: str):
    return session.method("groups.getById", {"group_id": groupId, "fields" : "activity,ban_info,can_post,can_see_all_posts,city,\
                                             contacts,counters,country,cover,description,finish_date,fixed_post,links,market,members_count,\
                                             place,site,start_date,status,verified,wiki_page"})

def getUsersInfo(session: vk_api.VkApi, userIds: str):
    return session.method("users.get", {"user_ids": userIds, "fields": "activities,about,blacklisted,blacklisted_by_me,books,\
                                        bdate,can_be_invited_group,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,\
                                        can_write_private_message,career,common_count,connections,contacts,city,country,crop_photo,\
                                        domain,education,exports,followers_count,friend_status,has_photo,has_mobile,home_town,photo_100,\
                                        photo_200,photo_200_orig,photo_400_orig,photo_50,sex,site,schools,screen_name,status,verified,\
                                        games,interests,is_favorite,is_friend,is_hidden_from_feed,last_seen,maiden_name,military,\
                                        movies,music,nickname,occupation,online,personal,photo_id,photo_max,photo_max_orig,quotes,\
                                        relation,relatives,timezone,tv,universities"})

def getPostsInfo(session: vk_api.VkApi, id: int, offset: int, count: int): # Возвращает словарь с count постами начиная с поста offset
    return session.method("wall.get", {"owner_id": id, "offset": offset, "count": count})


def getFriendsInfo(session: vk_api.VkApi, userId: int): # Возвращает словарь с количеством друзей, списком id друзей
    return session.method("friends.get", {"user_id": userId})


def writeJsonList(info, filename: str):
    with open(filename, 'w', encoding='utf8') as file:
        for i in info:
            json.dump(i, file, separators=(',', ':'), indent=4, ensure_ascii=False)
            file.write("\n")


def writeJson(info, filename: str):
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(info, file, separators=(',', ':'), indent=4, ensure_ascii=False)
        file.write("\n")


def isLink(link: str):
    return link.startswith("http")
    

def fromLinkToId(link: str):
    index = link.rfind("/")
    link = link[index + 1: len(link)+1]
    return link
    


if __name__ == "__main__":
    session = vk_api.VkApi(token=token)

    info = getGroupInfo(session, "215278139")
    writeJson(info, "215278139.json")

    lst = "freshentree9,v.dmkrt,tobuso"
    
    info = getUsersInfo(session, lst)
    writeJsonList(info, "users.json")

    link = "https://vk.com/sibguti_info"

    id = fromLinkToId(link)

    info = getGroupInfo(session, id)
    writeJson(info, id + ".json")

    info = getPostsInfo(session, -215278139, 0, 10)
    writeJson(info, id + "_wall.json")

    info = getFriendsInfo(session, 212184201)  # Получаем id друзей в info
    for friend in info["items"]:               # Вывод информации о каждом друге
        user = getUsersInfo(session, friend)
        print(f'{user[0]["first_name"]} {user[0]["last_name"]}')