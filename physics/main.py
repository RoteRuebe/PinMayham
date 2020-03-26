#!/usr/bin/env python3
import object, world, pygame
pygame.display.init()
screen = pygame.display.set_mode((500,500))

w = world.world(0.001,500,screen)

obj = object.object(0,450,10,1,w)
obj.apply_force((10,10))

while True:
    w.tick()
    w.draw(False)
    pygame.display.flip()
