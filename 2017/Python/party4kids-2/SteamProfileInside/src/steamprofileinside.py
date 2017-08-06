import requests
import json
from xml.dom.minidom import parseString
import math
import pygal

STEAM_API_KEY = '1644F282E1FBC5A3731DD84A220BA83E'
STEAM_USERNAME = 'Nagluzz'

user_web_info = requests.get('http://steamcommunity.com/id/{0}/games?tab=all&xml=1'.format(STEAM_USERNAME))
steamid = str(parseString(user_web_info.text.encode('utf-8')).getElementsByTagName('steamID64')[0].firstChild.wholeText)


friend_list_request = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={0}&steamid={1}&relationship=friend'.format(STEAM_API_KEY, steamid)
response = requests.get(friend_list_request)
#print(response.text)

response_json = json.loads(response.text)
friends_info = response_json["friendslist"]['friends'][0]['steamid']
all_friends = response_json["friendslist"]['friends']
friendsid = friends_info
#print(friendsid)


def get_friend_nick(friendid):
    player_summaries_request = ('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}'.format(STEAM_API_KEY, friendid))
    response = requests.get(player_summaries_request)
    nick = json.loads(response.text)
    friend_nick = nick["response"]["players"][0]["personaname"]
    return friend_nick
    

def get_csgo_time(friendid):
    friend_games_response = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={0}&steamid={1}&format=json'.format(STEAM_API_KEY, friendid)) #<Response [403]>
    #print(friend_games_response.text)

    response_json = json.loads(friend_games_response.text)
    friend_games = response_json["response"]["games"]
    csgo_time = 0
    for game in friend_games:
        if game['appid'] == 730:
            #print(game["playtime_forever"])
            csgo_time = game["playtime_forever"]
    hoursincsgo = csgo_time/60
    return math.ceil(hoursincsgo)


line_chart = pygal.Bar()
line_chart.title = 'Время проведенное в игре CS:GO'
for friend in all_friends:
    friendid = friend['steamid']
    friend_nick = get_friend_nick(friendid)
    csgo_time = get_csgo_time(friendid)
    line_chart.add(friend_nick, csgo_time)
    #print(get_friend_nick(friendid) +' '+ str(csgo_time))
My_nick = get_friend_nick(steamid)
My_time = get_csgo_time(steamid)
line_chart.add(My_nick, My_time)
line_chart.render_in_browser()
line_chart.render_to_file("result.svg")

#friend_list = requests.get(friend_list_request)
#print(friend_list.text)

#csgo_web = requests.get(csgo_web_response)
#print(csgo_web.text)
