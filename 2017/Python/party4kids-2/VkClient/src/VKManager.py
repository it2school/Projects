import time
import vk

login = input("Введите ваш номер телефона или email:")

#password = getpass.getpass()
password = input("Введите пароль:")

session = vk.AuthSession(app_id=5980149, user_login = login, user_password = password,scope = 1+2+4+8+1024)

#print("Маркер доступа:", session.access_token)

#session = vk.Session(access_token='')

api = vk.API(session)


def get_friend_data(user_id):
    user_info = api.users.get(user_ids=user_id, fields=('sex', 'bdate', 'nickname', 'country', 'education',
                                                                    'city', 'can_see_audio','about','books',
                                                        "contacts",'counters'))[0]
    first_name = user_info['first_name']
    last_name = user_info['last_name']
    print("--------------------")
    print("Имя пользователя -", first_name, last_name)
    if user_info["sex"] == 1:
        print("Пользователь женского пола")
    elif user_info["sex"] == 2:
        print("Пользователь мужского пола")
    if 'bdate' in user_info:
        birthday = user_info['bdate']
        print("Дата рождения:", birthday)
    else:
        print("Дата рождения неизвестна")
    if 'country' in user_info:
        country = user_info['country']
        print("Страна , в которой живет пользователь, называется:",country)
    else:
        print("Страна, где живет пользователь неизвестна")
    if 'city' in user_info:
        city = user_info['city']
        #citytranslated = api.database.getCitiesById(city[0])
        print("Город , в котором живет пользователь называется:",city)
    else:
        print("Город, в котором живет пользователь неизвестен")      
    if 'can_see_audio' in user_info:
        if user_info['can_see_audio'] == 1:
            print('У этого пользователя открыты аудиозаписи')
        else:
            print("У этого пользователя закрыты аудиозаписи")
    elif 'can_see_audio' in user_info:
        if user_info['can_see_audio'] == 0:
            print('У этого пользователя закрыты аудиозаписи')
        else:
            print('У этого пользователя закрыты аудиозаписи')
    else:
        print('У этого пользователя закрыты аудиозаписи')
    if 'education' in user_info:
        education = user_info['education']
        print('Пользователь учится в', education)
    else:
        print("Место учебы неизвестно")
    if 'books' in user_info:
        books = user_info['books']
        print("Любимые книги:",books)
    else:
        print("Любимые книги неизвестны")
    if 'mobile_phone' in user_info:
        mobile_phone = user_info['mobile_phone']
        print("Номер телефона пользователя:",mobile_phone)
    else:
        print("Номер телефона пользователя неизвестен")
    if 'home_phone' in user_info:
        home_phone = user_info['home_phone']
        print("Дополнительный номер телефона пользователя:",home_phone)
    else:
        print("Дополнительный номер пользователя неизвестен")
    counters = user_info['counters']
    if 'albums' in counters:
        albums = counters['albums']
        print("Кол-во альбомов:",albums)
    else:
        print("Кол-во альбомов неизвестно")
    if 'videos' in counters:
        videos = counters['videos']
        print("Кол-во видео:",videos)
    else:
        print("Кол-во видео неизвестно")
    if 'audios' in counters:
        audios = counters['audios']
        print("Кол-во аудио:",audios)
    else:
        print("Кол-во аудио неизвестно")
    if 'photos' in counters:
        photos = counters['photos']
        print("Кол-во фотографий:",photos)
    else:
        print("Кол-во фотографий неизвестно")
    if 'friends' in counters:
        friends = counters['friends']
        print("Кол-во друзей:",friends)
    else:
        print("Кол-во друзей неизвестно")
    if 'groups' in counters:
        groups = counters['groups']
        print("Кол-во групп:",groups)
    else:
        print("Кол-во групп неизвестно")
    if 'followers' in counters:
        followers = counters['followers']
        print("Кол-во подписчиков:",followers)
    else:
        print("Кол-во подписчиков неизвестно")
    print("--------------------")



def get_all_friends_info():
    friend_ids = api.friends.get()
    for friend_id in friend_ids:
        get_friend_data(friend_id)
        time.sleep(0.4)

get_all_friends_info()
#window.mainloop()