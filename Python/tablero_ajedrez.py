from pygame import *
import sys
import random

init()
screen = display.set_mode((800,600))
ancho,alto = 50,50

while True:
    for e in event.get():
        if e .type == QUIT:
            sys.exit()
    screen.fill('white')
    draw.rect(screen, ('black'), (100,100, 400, 400), 2)
    x = 100
    y = 100
    while x <=400:
        draw.rect(screen, ('black'), (x,100,ancho,alto), 0)
        x = x + 100
    x = 100
    while x <=400:
        draw.rect(screen, ('black'), (x,200,ancho,alto), 0)
        x = x + 100
    x = 100
    while x <=400:
        draw.rect(screen, ('black'), (x,300,ancho,alto), 0)
        x = x + 100
    x = 100
    while x <=400:
        draw.rect(screen, ('black'), (x,400,ancho,alto), 0)
        x = x + 100
    x = 150
    while x <=450:
        draw.rect(screen, ('black'), (x,150,ancho,alto), 0)
        x = x + 100
    x = 150
    while x <=450:
        draw.rect(screen, ('black'), (x,250,ancho,alto), 0)
        x = x+100
    x = 150
    while x <=450:
        draw.rect(screen, ('black'), (x,350,ancho,alto), 0)
        x = x+100
    x = 150
    while x <=450:
        draw.rect(screen, ('black'), (x,450,ancho,alto), 0)
        x = x+100
    
    display.flip()
