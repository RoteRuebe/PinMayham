#!/usr/bin/env python3
import object, pygame, time
pygame.display.init()
screen = pygame.display.set_mode((500,500))

gravity = 0.005

obj = object.object(100,450,50,1,gravity)
obj.apply_force((10,0))
ymin = 500

while True:
    obj.tick()
    if obj.y < ymin:
        ymin = obj.y
        print(ymin)

    obj.draw(screen)
    pygame.display.flip()
    