from turtle import *
from settings import *
from bisness import *



pure_goto(mideana)

def letter_K():
    position = pos()
    goto(sum_tuple(pos(),vector_up,(vector_right[0] / 2, vector_right[1] / 2))) 
    goto(sum_tuple(pos(), vector_down,(vector_right[0] / 2, vector_right[1] / 2)))
    pure_goto(position)

def letter_J():
    position = pos()
    pure_goto(sum_tuple(pos(),vector_up))
    goto(sum_tuple(pos(),vector_down,(vector_right[0] / 2, vector_right[1] / 2))) 
    goto(sum_tuple(pos(),vector_up,(vector_right[0] / 2, vector_right[1] / 2)))
    pure_goto(position)


def letter_W():
    position = pos()
    pure_goto(sum_tuple(pos(),vector_up))
    goto(sum_tuple(pos(),vector_down,(vector_right[0] / 2, vector_right[1] / 2))) 
    goto(sum_tuple(pos(),vector_up,(vector_right[0] / 2, vector_right[1] / 2)))
    pure_goto(position)
    center_dot(15)
       
def letter_X():
    position = pos()
    goto(sum_tuple(pos(),vector_up,(vector_right[0] / 2, vector_right[1] / 2))) 
    goto(sum_tuple(pos(),vector_down,(vector_right[0] / 2, vector_right[1] / 2)))
    pure_goto(position)
    center_dot(15)

def letter_L():
    position = pos()
    goto(sum_tuple(pos(),vector_right,(vector_up[0] / 2, vector_up[1] / 2 ))) 
    goto(sum_tuple(pos(),vector_left,(vector_up[0] / 2, vector_up[1] / 2 )))
    pure_goto(position)

def letter_Y():
    position = pos()
    goto(sum_tuple(pos(),vector_right,(vector_up[0] / 2, vector_up[1] / 2 ))) 
    goto(sum_tuple(pos(),vector_left,(vector_up[0] / 2, vector_up[1] / 2 )))
    pure_goto(position)
    center_dot(15)

def letter_M():
    position = pos()
    pure_goto(sum_tuple(pos(),vector_right))
    goto(sum_tuple(pos(),vector_left,(vector_up[0] / 2, vector_up[1] / 2 ))) 
    goto(sum_tuple(pos(),vector_right,(vector_up[0] / 2, vector_up[1] / 2 )))
    pure_goto(position)

def letter_Z():
    position = pos()
    pure_goto(sum_tuple(pos(),vector_right))
    goto(sum_tuple(pos(),vector_left,(vector_up[0] / 2, vector_up[1] / 2 )) )
    goto(sum_tuple(pos(),vector_right,(vector_up[0] / 2, vector_up[1] / 2 )))
    pure_goto(position)
    center_dot(15)

def letter_A():
    down_line()
    right_line()

def letter_B():
    left_line()
    down_line()
    right_line()

def letter_O():
    left_line()
    down_line()
    right_line()
    center_dot(15)

def letter_C():
    left_line()
    down_line()

def letter_P():
    left_line()
    down_line()
    center_dot(15)

def letter_D():
    down_line()
    upper_line()
    right_line()

def letter_E():
    down_line()
    upper_line()
    right_line()
    left_line()

def letter_R():
    down_line()
    upper_line()
    right_line()
    left_line()
    center_dot(15)

def letter_F():
    down_line()
    upper_line()
    left_line()
    
def letter_S():
    down_line()
    upper_line()
    left_line()
    center_dot(15)

def letter_Q():
    down_line()
    upper_line()
    right_line()
    center_dot(15)

def letter_N():
    down_line()
    right_line()
    center_dot(15)

def letter_G():
    upper_line()
    right_line()
    
def letter_T():
    upper_line()
    right_line()
    center_dot(15)

def letter_H():
    upper_line()
    right_line()
    left_line()

def letter_U():
    upper_line()
    right_line()
    left_line()
    center_dot(15)

def letter_I():
    upper_line()
    left_line()

def letter_V():  
    upper_line()
    left_line()
    center_dot(15)

def exec_letter(letter):
    current_funk = "letter_" + letter
    if current_funk in globals():
        globals()[current_funk]()


def next_line():
    mideana[1]-=letter_size+letter_speceing
    pure_goto(mideana)

def encript(text,mideana):
    text = text.upper()
    for letter in text:
        position = pos()
        
        if pos()[0]+letter_size > size[0]/2:
            next_line()
            position = pos()
        exec_letter(letter) 
        pure_goto(sum_tuple(position,vector_right,(letter_speceing, 0)))




# next_line()
print("Введите слово, которое нужно зашифровать(на английском языке):")
text = input()
encript(text,mideana)


#input()





