from pygame import *
import sys
import random

init()
screen = display.set_mode((800,600))
n = random.randint(5,10)
texto = font.SysFont('Calibri',40)

while True:
    for e in event.get():
        if e .type == QUIT:
            sys.exit()
    screen.fill('white')
    escalon = 0
    x, y, ancho = 0,550,800
    while escalon < n:
        draw.rect(screen, ('grey'), (x,y,ancho,50), 3)
        escalon = escalon + 1
        x = x+25
        y = y-50
        ancho = ancho-50
    letra = texto.render("Escalones: " +str(n), True, ('black'))
    screen.blit(letra, (10,0))
    display.flip()
    print(n)