from pygame import *
import sys, random

init()
screen = display.set_mode((800,600))
x, y = 100, 100
xs = []
ys = []

n =0
while True:
    for e in event.get():
        if e.type == QUIT: sys.exit() 
        if e.type == MOUSEBUTTONDOWN and e.button==1:
         x, y = random.randint(0,800), random.randint(0,600)
         xs.append(x)
         ys.append(y)
    
    screen.fill((255,255,255))    
    for i in range(len(xs)):
        draw.circle(screen, (0,0,0), (xs[i],ys[i]), 30, 0)
        if i >=1:
            draw.line(screen, (0,0,0), (xs[i-1], ys[i-1]), (xs[i], ys[i]), 10)
    
    display.flip()

