#!/usr/bin/env python3

class world:
    def __init__(self,gravity,size,surface):
        self.gravity = gravity
        self.size = size
        self.surface = surface
        self.entitys = []
        
    def tick(self):
        for entity in self.entitys:
            entity.tick()
            
    def draw(self):
        self.surface.fill((0,0,0))
        for entity in self.entitys:
            entity.draw()
            
    def collide(x,y):
        if y < 0:
            return 0
        if x > 500:
            return 1
        if y > 500:
            return 2
        if x < 0:
            return 3
        
    def register(self,other):
        self.entitys.append(other)
        self.draw()
        
