from turtle import *
border = 20
letter_size = 100
letter_speceing = 20
size = [800, 600]
mideana =[0, 0] 
mideana[0] = - size[0] / 2 + border 
mideana[1] = size[1] / 2 - border - letter_size
screen = Screen()
screen.setup(*size)
#setup(*size)
screen.bgcolor("lightgray")
color("blue")
width(4)
speed(0)

vector_up = (0, 100)
vector_down = (0, -100)
vector_left = (-100,0)
vector_right = (100,0)
