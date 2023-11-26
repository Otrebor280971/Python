import pygame
import random


pygame.init()

ventana_ancho = 600
ventana_alto = 600

N = 10
tamano_casilla = ventana_ancho // N

color_fondo = ('white')
color_ficha = ('green')

ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))

fila_ficha = random.randint(0, N - 1)
columna_ficha = random.randint(0, N - 1)

def tablero():
    ventana.fill(color_fondo)

    for fila in range(N):
        for columna in range(N):
            pygame.draw.rect(ventana, ('black'), (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla), 1)

    ficha_x = columna_ficha * tamano_casilla
    ficha_y = fila_ficha * tamano_casilla
    pygame.draw.rect(ventana, color_ficha, (ficha_x, ficha_y, tamano_casilla, tamano_casilla))


clock = pygame.time.Clock()

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fila_ficha = max(fila_ficha - 1, 0)

            elif event.key == pygame.K_DOWN:
                fila_ficha = min(fila_ficha + 1, N - 1)

            elif event.key == pygame.K_LEFT:
                columna_ficha = max(columna_ficha - 1, 0)

            elif event.key == pygame.K_RIGHT:
                columna_ficha = min(columna_ficha + 1, N - 1)

    tablero()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
