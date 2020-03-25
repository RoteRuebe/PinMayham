#!/usr/bin/env python3
import pygame

class object:
    def __init__ (self,x,y,m,l,gravity = 0):
        self.x = x
        self.y = y
        self.l = l
        self.m = m
        self.gravity = gravity
        self.f = [0,0]
        
    def tick (self):
        self.x += self.f[0]/self.m
        self.y += self.f[1]/self.m
        self.accelerate((0,self.gravity))
        
        if self.x > 500-self.l or self.x < 0:
            self.f[0] *= -1
        
        if self.y > 500-self.l or self.y < 0:
            self.f[1] *= -1
        
    def draw(self,surface):
        surface.fill((255,255,255),pygame.Rect(self.x,self.y,self.l,self.l))
        
    def apply_force(self,f):
        self.f[0] += f[0]
        self.f[1] += f[1]
        
    def accelerate(self,v):
        self.f[0] += v[0] * self.m
        self.f[1] += v[1] * self.m