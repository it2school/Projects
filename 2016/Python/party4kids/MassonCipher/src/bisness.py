from turtle import *
from settings import *

def pure_turtle(action):
    up()
    action()
    down()

def pure_goto(point):
    pure_turtle(lambda: goto(point))

def center_dot(size):
    position = pos()
    pure_goto(sum_tuple(position,(letter_size / 2, letter_size / 2)))
    dot(size)
    pure_goto(position)

def down_line():
    position = pos()
    goto(sum_tuple(pos(),(vector_right)))
    pure_goto(position)

def upper_line():
    position = pos()
    pure_goto(sum_tuple(pos(), vector_up))
    goto(sum_tuple(pos(),vector_right))
    pure_goto(position) 
    
def left_line():
    position = pos()
    goto(sum_tuple(pos(),vector_up))
    pure_goto(position)

def right_line():
    position = pos()
    pure_goto(sum_tuple(pos(),vector_right))
    goto(sum_tuple(pos(),vector_up))
    pure_goto(position)
    
    
def sum_tuple(*args):
  result = map(sum, zip(*args))
  return result