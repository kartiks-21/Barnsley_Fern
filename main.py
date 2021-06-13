import pygame
from pygame import gfxdraw
import random

pygame.init()

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Barnsley Fern")

xi = 0
yi = 0

def f1(x,y):
    xn = 0
    yn = 0.16*y
    return xn,yn

def f2(x,y):
    xn = 0.85*x + 0.04*y
    yn = -0.04*x + 0.85*y + 1.6
    return xn, yn

def f3(x,y):
    xn = 0.20*x - 0.26*y
    yn = 0.23*x + 0.22*y + 1.6
    return xn, yn

def f4(x,y):
    xn = -0.15*x + 0.28*y
    yn = 0.26*x + 0.24*y + 0.44
    return xn, yn

def point(x,y):
    color = (0,255,0)
    pos = (x,y)
    screen.fill(color, (pos, (1, 1)))


def mainloop():
    running = True
    while(running):
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        xi = 0
        yi = 0

        for i in range(1,30000):
            point(70*xi + 500, 65*yi + 100)
            a = random.random()
            a = a * 100
            xn = xi
            yn = yi

            if(a<1):
                xi,yi = f1(xn,yn)
            elif(a<86):
                xi,yi = f2(xn,yn)
            elif(a<93):
                xi,yi = f3(xn,yn)
            else:
                xi,yi = f4(xn,yn)


        pygame.display.update()

mainloop()