import vk_api
import json

from vk_api.execute import VkFunction

# https://oauth.vk.com/authorize?&display=page&redirect_url=https://oauth.vk.com/blank.html&scope=offline,friends,wall,status,docs,groups&response_type=token&v=5.21
# Запрос на access token

def getGroupInfo(session: vk_api.VkApi, groupId: str): # Задание 2.1
    return session.method("groups.getById", {"group_id": groupId, "fields" : "activity,ban_info,can_post,can_see_all_posts,city,\
                                             contacts,counters,country,cover,description,finish_date,fixed_post,links,market,members_count,\
                                             place,site,start_date,status,verified,wiki_page"})

def getUsersInfo(session: vk_api.VkApi, userIds: str): # Задание 2.2
    return session.method("users.get", {"user_ids": userIds, "fields": "activities,about,blacklisted,blacklisted_by_me,books,\
                                        bdate,can_be_invited_group,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,\
                                        can_write_private_message,career,common_count,connections,contacts,city,country,crop_photo,\
                                        domain,education,exports,followers_count,friend_status,has_photo,has_mobile,home_town,photo_100,\
                                        photo_200,photo_200_orig,photo_400_orig,photo_50,sex,site,schools,screen_name,status,verified,\
                                        games,interests,is_favorite,is_friend,is_hidden_from_feed,last_seen,maiden_name,military,\
                                        movies,music,nickname,occupation,online,personal,photo_id,photo_max,photo_max_orig,quotes,\
                                        relation,relatives,timezone,tv,universities"})

def getUsersInfoVKScript(session: vk_api.VkApi, userIds: str): # Задание 2.3
    vk = session.get_api()
    return vk_get_users_info(vk, {"user_ids": "freshentree9", "fields": "activities,about,blacklisted,blacklisted_by_me,books,\
                                        bdate,can_be_invited_group,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,\
                                        can_write_private_message,career,common_count,connections,contacts,city,country,crop_photo,\
                                        domain,education,exports,followers_count,friend_status,has_photo,has_mobile,home_town,photo_100,\
                                        photo_200,photo_200_orig,photo_400_orig,photo_50,sex,site,schools,screen_name,status,verified,\
                                        games,interests,is_favorite,is_friend,is_hidden_from_feed,last_seen,maiden_name,military,\
                                        movies,music,nickname,occupation,online,personal,photo_id,photo_max,photo_max_orig,quotes,\
                                        relation,relatives,timezone,tv,universities"})

vk_get_users_info = VkFunction(args=('values',), code='''
    return API.users.get(%(values)s);
''')


def getFullWall(session: vk_api.VkApi, owner_id: int): # Возвращает словарь с количеством записей и списком записей
    tools = vk_api.VkTools(session)
    wall = tools.get_all('wall.get', 100, {'owner_id': owner_id})
    print('Posts count:', wall['count'])
    return wall

def getPostsInfo(session: vk_api.VkApi, id: int, offset: int, count: int): # Возвращает словарь с count постами начиная с поста offset
    return session.method("wall.get", {"owner_id": id, "offset": offset, "count": count})

def getFriendsInfo(session: vk_api.VkApi, userId: int): # Возвращает словарь с количеством друзей и списком id друзей
    return session.method("friends.get", {"user_id": userId})

def getUserStatus(session: vk_api.VkApi, userId: int):
    return session.method("status.get", {"user_id": userId})

def getGroupStatus(session: vk_api.VkApi, groupId: int):
    return session.method("status.get", {"group_id": groupId})


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
    

def fromLinkToIdGroup(session: vk_api.VkApi, link: str):

    index = link.rfind("/")
    link = link[index + 1: len(link)+1]

    group = getGroupInfo(session, link)

    groupId = group[0]["id"]

    print(groupId)

    return int(groupId)
    
def fromLinkToIdUser(session: vk_api.VkApi, link: str):

    index = link.rfind("/")
    link = link[index + 1: len(link)+1]

    user = getUsersInfo(session, link)

    userId = user[0]["id"]

    print(userId)

    return int(userId)

def auth_handler():
    # """ При двухфакторной аутентификации вызывается эта функция.
    # """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = False

    return key, remember_device

def captcha_handler(captcha):
    #     При возникновении капчи вызывается эта функция и ей передается объект 
    #     капчи. Через метод get_url можно получить ссылку на изображение.
    #     Через метод try_again можно попытаться отправить запрос с кодом капчи 


    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


def twoFactorAuth(session: vk_api.VkApi):
    # """ Пример обработки двухфакторной аутентификации """

    try:
        session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return


def main():
    session = vk_api.VkApi(login=login,
                           password=password,
                           token=token,
                           app_id=app_id,
                           scope="offline,friends,wall,status,docs,groups",
                           client_secret=service_key,
                           auth_handler=auth_handler,
                           captcha_handler=captcha_handler)

    vk = session.get_api()

    # info = getGroupInfo(session, "215278139")
    # writeJson(info, "215278139.json")

    # lst = "freshentree9,v.dmkrt,tobuso"
    
    # info = getUsersInfo(session, lst)
    # writeJsonList(info, "users.json")

    # link = "https://vk.com/hakatonurtisi"

    # id = fromLinkToIdGroup(session, link)

    # info = getGroupInfo(session, id)
    # writeJson(info, str(id) + ".json")

    # info = getPostsInfo(session, -215278139, 0, 10)
    # writeJson(info, str(id) + "_wall.json")

    # info = getFriendsInfo(session, 212184201)  # Получаем id друзей в info
    # for friend in info["items"]:               # Вывод информации о каждом друге
    #     user = getUsersInfo(session, friend)
    #     print(f'{user[0]["first_name"]} {user[0]["last_name"]}')

    # wall = getFullWall(session, -187227252)
    # writeJson(wall, 'trrrhachatrrrhahaa.json')

    # if (isLink(link)):
    #     link = fromLinkToIdGroup(session, link)

    # wall = getFullWall(session, -215278139)
    
    # writeJson(wall, 'trrrhachatrrrhahaa.json')

    print(getUsersInfoVKScript(session, 'freshentree9')[0]["first_name"])
    

if __name__ == "__main__":
    main()