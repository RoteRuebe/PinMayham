#!/usr/bin/env python3
import object, world, pygame
from math import *
pygame.display.init()
screen = pygame.display.set_mode((1000,1000))

w = world.world(0.001,1000,screen)

obj1 = object.physical_object(0,0,10,10,w)
obj1.apply_force((0,0))

obj2 = object.physical_object(450,450,10,10,w)
obj2.apply_force((10,10))

well = object.physical_object(450,450,50,50,w)

def gravitate(sat,pla):
    print(sat.x,sat.y)
    print(pla.x,pla.y)
    dx = abs(sat.x-pla.x)
    dy = abs(sat.y-pla.y)
    d = sqrt(dx**2+dy**2)
    g = 1
    vl = g/d
    print(dx*vl,dy*vl)
    sat.apply_force((dx*vl,dy*vl))

while True:
    w.tick()
    gravitate(obj1,well)
    w.draw()
    pygame.display.flip()
