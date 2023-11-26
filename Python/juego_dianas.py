from pygame import *
import sys
import math, random

init()
screen = display.set_mode((600,600))
texto = font.SysFont('Calibri', 40)
#Raíz de las diferenias de x y y

x1 = random.randint(20,580)
y1 = random.randint(20,580)
x2 = random.randint(20,580)
y2 = random.randint(20,580)
x3 = random.randint(20,580)
y3 = random.randint(20,580)

disparo_1 = (x1,y1)
disparo_2 = (x2,y2)
disparo_3 = (x3,y3)

puntos = 0

distancia_tiro_1 = math.sqrt((300-x1)**2 + (300-y1)**2)
distancia_tiro_2 = math.sqrt((300-x2)**2 + (300-y2)**2)
distancia_tiro_3 = math.sqrt((300-x3)**2 + (300-y3)**2)

if distancia_tiro_1 <= 65:
    puntos = puntos + 100
elif distancia_tiro_1 <= 165:
    puntos = puntos + 50
elif distancia_tiro_1 <= 265:
    puntos = puntos + 20

if distancia_tiro_2 <= 65:
    puntos = puntos + 100
elif distancia_tiro_2 <= 165:
    puntos = puntos + 50
elif distancia_tiro_2 <= 265:
    puntos = puntos + 20

if distancia_tiro_3 <= 65:
    puntos = puntos + 100
elif distancia_tiro_3 <= 165:
    puntos = puntos + 50
elif distancia_tiro_3 <= 265:
    puntos = puntos + 20



while True:
    screen.fill('grey')
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
    
    puntaje = texto.render("Puntos: " + str(puntos), True, ('white'))
    screen.blit(puntaje,(100,0))
            
    draw.circle(screen, ('blue'), (300,300), 250, 0)
    draw.circle(screen, ('green'), (300,300), 150, 0)
    draw.circle(screen, ('red'), (300,300), 50, 0)
    
    tiro_1 = draw.circle(screen, ('black'), (x1,y1), 20, 0)
    tiro_2 = draw.circle(screen, ('black'), (x2,y2), 20, 0)
    tiro_3 = draw.circle(screen, ('black'), (x3,y3), 20, 0)

    display.flip()