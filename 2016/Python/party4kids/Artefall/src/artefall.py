#Program by Artefall
from random import *

enemylife = int
enemypower = int
HP = int
POW = int
AGI = int


def elife(enemy):
    print("Кол-во HP вашего противника -", enemy['health'])

def error():
    print("Такого варианта не существует")
    
def mylife(player):
    print("Кол-во вашего HP -",player["HP"])
    
def randomenemy():
    Zombie = {'name': "зомби",'health':50,'power':5}
    Bandit = {'name': "бандит",'health':150,'power':20}
    enemy = randint(1,2)
    if enemy == 1:
        return Zombie
    elif enemy == 2:
        return Bandit
        
def fightsystem(player):
    enemy = randomenemy()
    print("Ваш противник - ", enemy["name"])
    while enemy['health'] > 0:
        mylife(player)
        elife(enemy)
        print("Вы наносите противнику удар -", player["POW"], " hp")
        enemy['health'] = (enemy['health'] - player["POW"])
        print("Вам нанесли удар - ",  enemy["power"], " hp")
        player["HP"] = player["HP"] - enemy["power"]
    print("Это победа вы победили вашего первого противника. И теперь можно двигаться дальше.")
        
nickname = input("""Вас приветствует текстовое RPGhhh
Введите ваш никнэйм:""")

print("Привет,", nickname)

RPGclass = int(input("""Введите номер класса:
[1] - Полицейский
Здоровье - 450
Сила - 15
Ловкость - 50
[2] - Пожарный
Здоровье - 450
Сила - 20
Ловкость - 20
[3] - Бандит
Здоровье - 400
Сила - 20
Ловкость - 40
[4] - Бездомный
Здоровье - 350
Сила - 25
Ловкость - 20
"""))

if RPGclass == 1:
    player = {'HP':450,'POW':15,'AGI':50}
    HP = 450
    POW = 15
    AGI = 50   
elif RPGclass == 2:
    player = {'HP':450,'POW':20,'AGI':20}
    HP = 450
    POW = 20
    AGI = 20   
elif RPGclass == 3:
    player = {'HP':400,'POW':20,'AGI':40}
    HP = 400
    POW = 20
    AGI = 40  
elif RPGclass == 4:
    player = {'HP':350,'POW':25,'AGI':20}
    HP = 350
    POW = 25
    AGI = 20
else:
    error()
    exit(0)
    
print("""Ну , что же , апокалипсис на дворе, вам нужно выжить! И чем больше дней - тем лучше (кто знает может вам удасться пережить его )
Начнём же!

Вы очнулись в больнице, вы встали , посмотрели в окно и поняли что на улице творится анархия: Машины разбросаны
, огромное количество домов охватил огонь
""")

fightsystem(player)


