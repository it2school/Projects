from tkinter import *
from PIL import ImageTk, Image
import os

class Hero():
  def __init__(self,name,hp,atack,mana):
    self.name = name
    self.hp = hp
    self.atack = atack
    self.mana = mana
  def attack(self,enemy):
    enemy.hp = enemy.hp - self.atack
    story.insert(END,"Вы атаковали.Вы нанесли 15 урона")
    self.hp = self.hp - enemy.atack
    story.insert(END,"Противник атаковал.Противник нанес 20 урона")
  def defence(self,enemy):
    self.hp = self.hp + self.atack
    story.insert(END,"Вы защищались.Вы заблокировали 15 урона")
    self.hp = self.hp - enemy.atack
    story.insert(END,"Противник атаковал.Противник нанес 5 урона")

class Enemy():
  def __init__(self,name,hp,atack,mana):
    self.name = name
    self.hp = hp
    self.atack = atack
    self.mana = mana

def attackButton():
    heralt.attack(imlerih)
    enemy_stat = Label(root, text = "{}\n Характеристики: \n Жизнь:{}\nАтака:{}\nМана:{}".format(imlerih.name, imlerih.hp , imlerih.atack , imlerih.mana))
    enemy_stat.grid(row=1, column = 3)
    player_stat = Label(root, text = "{}\n Характеристики: \n Жизнь:{}\nАтака:{}\nМана:{}".format(heralt.name, heralt.hp , heralt.atack , heralt.mana))
    player_stat.grid(row=1, column = 1)
    if imlerih.hp < 0:
        story.insert(END,"Вы победили")

def defencekButton():
    heralt.defence(imlerih)
    enemy_stat = Label(root, text = "{}\n Характеристики: \n Жизнь:{}\nАтака:{}\nМана:{}".format(imlerih.name, imlerih.hp , imlerih.atack , imlerih.mana))
    enemy_stat.grid(row=1, column = 3)
    player_stat = Label(root, text = "{}\n Характеристики: \n Жизнь:{}\nАтака:{}\nМана:{}".format(heralt.name, heralt.hp , heralt.atack , heralt.mana))
    player_stat.grid(row=1, column = 1)

heralt = Hero("Геральт",100,50,50)
imlerih = Enemy("Имлерих",500,20,1000)

root = Tk()

text1 = Label(root, text = "Вы:")
text1.grid(row=0, column = 0)

text2 = Label(root, text = "Противник:")
text2.grid(row=0, column = 2)

img = ImageTk.PhotoImage(Image.open("geralt.png"))
panel = Label(root, image = img)
panel.grid(row=1,column=0)

img2 = ImageTk.PhotoImage(Image.open("imlerih.png"))
panel2 = Label(root, image = img2)
panel2.grid(row=1, column = 2)

player_stat = Label(root, text = "{}\n Характеристики: \n Жизнь:{}\nАтака:{}\nМана:{}".format(heralt.name, heralt.hp , heralt.atack , heralt.mana))
player_stat.grid(row=1, column = 1)

enemy_stat = Label(root, text = "{}\n Характеристики: \n Жизнь:{}\nАтака:{}\nМана:{}".format(imlerih.name, imlerih.hp , imlerih.atack , imlerih.mana))
enemy_stat.grid(row=1, column = 3)

text3 = Label(root, text = "Действия:")
text3.grid(row=2, column = 0)

action1 = Button(root, text = "Атака", command = attackButton )
action1.grid(row=3, column = 0)

action2 = Button(root, text = "Защита",command = defencekButton)
action2.grid(row=4, column = 0)

action3 = Button(root, text = "Убежать")
action3.grid(row=5, column = 0)

global story
story = Listbox(root)
story.insert(1,"Сражение с Имлерихом началось")
story.grid(row=6, column = 0, columnspan=4, sticky="nsew")

root.mainloop()