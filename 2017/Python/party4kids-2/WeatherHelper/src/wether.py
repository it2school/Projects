from tkinter import *
from requests import *
import re

places = [
          {"name": "на речке Тилигул", "coords" : { "lat" : 47.6100218, "lon" : 30.2974534 } },
          {"name": "на Южном Буге", "coords" : { "lat" : 48.1621294, "lon" : 30.4145219 } },
          {"name": "на речке Северский Донецк", "coords" : { "lat" : 50.0010084, "lon" : 36.8625801 } },
          {"name": "на Хаджибейском лимане", "coords" : { "lat" : 46.691742, "lon" : 30.5175609 } },
          {"name": "на Днестрe", "coords" : { "lat" : 46.4894743, "lon" : 29.9935415 } },
          {"name": "на Сухoм лимaне", "coords" : { "lat" : 46.4022457, "lon" : 30.6354446 } },
          {"name": "на Днепре", "coords" : { "lat" : 48.4946839, "lon" : 34.918532 } },

]

def format_coords(coords):
    return str(coords["lat"]) + "," + str(coords["lon"])

def parse_coords(s):
    lat, lon = s.split(',')
    return {"lat": lat, "lon": lon}

def print_result(text):
    result.config(state=NORMAL)
    result.delete(1.0, END)
    result.insert(END, text)
    result.config(state=DISABLED)


def get_weather(payload, name=None):
    answer = get("http://api.openweathermap.org/data/2.5/weather?appid=56e6d7b1d0c97ffa78f3c3ed24a4095a", params=payload).json()
    # Словари и несколькими ключами:
    main_info = answer.get("main")
    wind_info = answer.get("wind")
    

    #Словари с одним ключем:
    clouds_info = answer.get("clouds")
    city = answer.get("name")

    #Дополнительная информация из главных словарей:
    main_humidity_info = main_info.get("humidity")
    main_temp_info = main_info.get("temp") # 274 Кельвина = 1 Цельсий
    wind_speed_info = wind_info.get("speed")
    main_pressure_info = main_info.get("pressure")
    #Готовая информация(переконвертированная)

    final_clouds = "".join(re.findall('(\d+)', str(clouds_info)))
    final_main_temp = str((round(main_temp_info) - 274))
    final_wind_speed = str(wind_speed_info)
    final_main_humidity = str(main_humidity_info)
    final_main_pressure = str(round(main_pressure_info * 0.75))
    final_city = "В городе " + city
    coords_input.delete(0, END)
    coords_input.insert(0, format_coords(payload))

    
    #Вывод информации о погоде на экран:
    print_result("""{} сегодня:

Tемпература:  {}° Цельсия;
Облачность: {}%;
Скорость ветра: {} м/с;
Влажность:  {}%
Атмосферное давление {} ммРc""".format(name or final_city, final_main_temp, final_clouds, final_wind_speed, final_main_humidity, final_main_pressure) )

root = Tk()

root.title("Погода на рыбалке")

root.resizable(False, False)

header = Label(root, text="Выберите место для рыбалки:", font="Helvetica 36",bg = "#c9dafc")
header.grid(row=0)

places_frame = Frame(root)
places_frame.grid(row=1)

def bind_prediction(i, place):
    name = place["name"]
    coords = place["coords"]
    button = Button(places_frame, text=place["name"], bg = "#ccdfff")
    button.bind("<Button-1>", lambda _: get_weather(coords, name))
    button.grid(row=i//4, column=i%4, sticky=W+E+N+S)

for i, place in enumerate(places):
    bind_prediction(i, place)

i += 1
my_coords_button = Button(places_frame, text="Свои координаты", bg = "#ccdfff")
my_coords_button.bind(
    "<Button-1>",
    lambda _: get_weather(parse_coords(coords_input.get()))
)
my_coords_button.grid(row=i//4, column=i%4, sticky=W+E+N+S)

coords_label = Label(places_frame, text="Координаты:")
coords_label.grid(row=i//4+1, sticky=E)
coords_input = Entry(places_frame, bg = "#f9fbff")
coords_input.grid(row=i//4+1, column=1, columnspan=3, sticky=W+E+N+S)

result = Text(root, bg = "#ccdfff")
result.grid(row=2, sticky=W+E+N+S)

root.mainloop()
