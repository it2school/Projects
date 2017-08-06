from turtle import*
from math import*
import os
from random import randint
scr = Screen()
scr.setup(800,600)
exitt = ("play")
while exitt == "play":
 print('''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
 result = Turtle()
 result.color('white')
 result.hideturtle()
 target = randint(-240,20)
 target = int(target)
 target_low = (target - 15)
 target_top = (target + 15)
 m = Turtle()
 m.color("blue")
 m.shape("circle")
 m.penup()
 m.goto(320,target)
 colormode(255)
 qqq = (0)
 for i in range(3):
    s = Turtle()
    s.color("red")
    s.penup()
    s.goto(-180,0)
    s.pendown()
    s.speed(0)
    result.undo()
    result.color('white')
    a = input("Площадь крыла(1 - 10см2) - ")
    a = float(a)
    if a < 0 or a > 11:
      print("CodeError")
      break
    
    b = input("Угол броска относительно горизонтали(-80 - 90) - ")
    b = float(b)
    if b < -81 or b > 91:
      print("CodeError")
      break
    
    c = input("Первоночальная скорость(1м/сек - 30м/сек) - ")
    c = float(c)
    if c < -1 or c > 31:
      print("CodeError")
      break
    
    s.speed(0)
    g = (0.22)
    p = (c * (a/50))
    
    x1 = (-180)
    y1 = (0)
    x2 = (x1 + c * cos(b * pi / 180))
    y2 = (y1 + c * sin(b * pi / 180))
    s.goto(x2,y2)
    #print(x2,y2)
    
    while x2 < 320 and x2 > -320 and y2 < 320 and y2 > -350:
        x0 = (x1)
        y0 = (y1)
        x1 = (x2)
        y1 = (y2)
        b = (atan((y1 - y0) / (x1 - x0)))
        c = ((y1 - y0) / sin(b))
        c = (c * 0.95)
        x2 = (x1 + c * cos(b))
        y2 = (y1 + c * sin(b))
        p = (c * (a/50))
        x2 = (x2 - p * sin(b))
        y2 = (y2 + p * cos(b))
        y2 = (y2 - g)
        s.goto(x2,y2)
    s.hideturtle()
        
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    if y1 < target_low or y1 > target_top:
        result.color(red,green,blue)
        result.penup()
        result.goto(0,80)
        result.pendown()
        st1 = ("Comic Sans Ms", 50, "bold")
        result.write("You lose!", font=st1)
    else:
        qqq = (1)
        result.color(red,green,blue)
        result.penup()
        result.goto(0,80)
        result.pendown()
        st1 = ("Comic Sans Ms", 50, "bold")
        result.write("You WON!", font=st1)
    print("---------------------------")
 exitt = input("To exit write exit ,to play write play : ")
 #m.reset()
 #s.reset()
 #os.system('clear')
 #result.reset()
 scr.clear()
exit()
