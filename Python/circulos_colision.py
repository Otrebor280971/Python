from pygame import *
import sys
import math, random

init()
screen = display.set_mode((600,600))

x1 = random.randint(0,600)
y1 = random.randint(0,600)
x2 = random.randint(0,600)
y2 = random.randint(0,600)

color = 'white'

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if distancia <= 400:
    color = 'red'
else:
    color = 'white'


while True:
    screen.fill('grey')
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
    
    crcl_grnd = draw.circle(screen, color, (x1,y1), 300, 0)
    crcl_pq = draw.circle(screen, color, (x2,y2), 100, 0)

    display.flip()