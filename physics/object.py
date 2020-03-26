#!/usr/bin/env python3
import pygame
import pygame.gfxdraw
import numpy as nm

class object:
    def __init__ (self,x,y,m,l,world):
        self.x = x
        self.y = y
        self.l = l
        self.m = m
        self.world = world
        self.world.register(self)
        self.f = [0,0]
        
    def tick(self,gravitate=None):
        self.gravitate(gravitate)
        self.x += self.f[0]/self.m
        self.y += self.f[1]/self.m
        return self.x,self.y
        
    def gravitate(self,other=None):
        if other == None:
            self.accelerate((0,self.world.gravity))
        else:
            dx = self.x - other[0]
            dy = self.y - other[1]
            q =  (self.world.gravity**2*dx**2-dy**2)/2
            x = -dy/2 + nm.sqrt((dy/2)**2-q)
            y = x*dy/dx
            self.accelerate((x,y))
        
    def draw(self):
        rect = pygame.Rect(self.x,self.y,self.l,self.l)
        self.world.surface.fill((255,255,255),rect)
        
    def apply_force(self,f):
        self.f[0] += f[0]
        self.f[1] += f[1]
        
    def accelerate(self,v):
        self.f[0] += v[0] * self.m
        self.f[1] += v[1] * self.m