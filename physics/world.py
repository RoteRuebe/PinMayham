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
            
    def draw(self,delete=True):
        if delete:  self.surface.fill((0,0,0))
        for entity in self.entitys:
            entity.draw()
            
    def collide(self,l,x,y=None):
        if y == None:
            y = x[1]
            x = x[0]
            
        colliding = []
            
        if y < 0:
            colliding.append(0)
        if x + l > self.size:
            colliding.append(1)
        if y + l > self.size:
            colliding.append(2)
        if x < 0:
            colliding.append(3)
        
        return colliding
        
    def register(self,other):
        self.entitys.append(other)
        self.draw()
        
