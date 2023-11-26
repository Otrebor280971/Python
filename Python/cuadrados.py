from pygame import *
import sys
import math, random

init()
screen = display.set_mode((600,600))

tamaño = random.randint(100,300)
x1 = random.randint(150,450)
y1 = random.randint(150,450)
x2 = random.randint(150,450)
y2 = random.randint(150,450)

color = 'white'

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if distancia <= tamaño:
    color = 'red'
else:
    color = 'white'

while True:
    screen.fill('grey')
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
    
    cdr_1 = draw.rect(screen, color, (x1, y1, tamaño, tamaño), 0)
    cdr_2 = draw.rect(screen, color, (x2, y2, tamaño, tamaño), 0)


    display.flip()