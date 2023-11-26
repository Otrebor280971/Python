from pygame import *
import sys

init()
screen = display.set_mode((800,600))
clock = time.Clock()
x=0
vel = 5
color = 'white'
while True:
    for e in event.get():
        if e .type == QUIT:
            sys.exit()
        if e.type ==MOUSEBUTTONDOWN and e.button == 1:
            x,y = mouse.get_pos()
            
    screen.fill('black')
    draw.circle(screen, (color), (x,100), 50, 0)
    x=x + vel
    if x>=750:
        vel =-5
        color= 'blue'
    elif x<=50:
        vel=5
        color='white'
    display.flip()
    clock.tick(60)