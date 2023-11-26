from pygame import *
import sys

init()
screen = display.set_mode((800,600))

def menu(screen):
    clock = time.Clock()
    x=0
    vel = 5
    color = 'red'
    fondo = image.load("pantalla_inicio.png")
    fondo = transform.scale(fondo, (800,600))
    pelota = image.load("pelota.png")
    pelota = transform.scale(pelota, (100,100))
    while True:
        for e in event.get():
            if e .type == QUIT:
                sys.exit()
            if e.type ==MOUSEBUTTONDOWN and e.button == 1:
                xp,yp = mouse.get_pos()
                return 2
        screen.blit(fondo, (0,0))
        draw.circle(screen, (color), (x,100), 50, 0)
        screen.blit(pelota, (x-50,50))
        x=x + vel
        if x>=750:
            vel =-5
            color= 'blue'
        elif x<=50:
            vel=5
            color='red'
        display.flip()
        clock.tick(60)
        
def escena_1(screen):
    clock = time.Clock()
    while True:
        for e in event.get():
            if e .type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                xp,yp = mouse.get_pos()
                return 1
            
        screen.fill('black')
        draw.circle(screen, ('white'), (400,300), 50, 0)
        display.flip()
        clock.tick(60)
        
escena = 1
while True:
    if escena == 1:
        escena =menu(screen)
    elif escena == 2:
       escena = escena_1(screen)
