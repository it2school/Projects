import pygame
import math
import sys
from pygame.locals import *

TURN_SPEED = 10
ACCELERATION = 2
MAX_FORWARD_SPEED = 10
MAX_REVERSE_SPEED = 5
BG= (0,0,0)
MAX_Y = 768
MAX_X = 1024


screen = pygame.display.set_mode((MAX_X, MAX_Y))
car = pygame.image.load('car1.png')
clock = pygame.time.Clock() 
k_up = k_down = k_left = k_right = 0 
speed = direction = 0 
position = (100, 100)


play = True
while play:
   
    clock.tick(30)

    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        
        down = event.type == KEYDOWN         
        if event.key == K_RIGHT:
            k_right = down * TURN_SPEED
        elif event.key == K_LEFT:
            k_left = down * TURN_SPEED
        elif event.key == K_UP:
            k_up = down * ACCELERATION
        elif event.key == K_DOWN:
            k_down = down * ACCELERATION
        elif event.key == K_RETURN:
            horn.play() 
        elif event.key == K_ESCAPE:
            play = False            
    screen.fill(BG)
    
    speed += (k_up - k_down)
    if speed > MAX_FORWARD_SPEED:
        speed = MAX_FORWARD_SPEED
    if speed < MAX_REVERSE_SPEED:
        speed = MAX_REVERSE_SPEED
    direction += (k_right - k_left)
    
    x, y = position
    rad = direction * math.pi / 180
    x += speed*math.sin(rad)
    y += speed*math.cos(rad)
    if y < 0:
        y = 0 
    elif y > MAX_Y:
        y = MAX_Y
    if x < 0:
        x = 0
    elif x > MAX_X:
        x = MAX_X        
    position = (x, y)
    
    rotated = pygame.transform.rotate(car, direction)
    
    rect = rotated.get_rect()
    rect.center = position
    print = position 
    
    screen.blit(rotated, rect)
    pygame.display.flip()

sys.exit(0) 