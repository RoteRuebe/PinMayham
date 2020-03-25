#!/usr/bin/env python3
import entity

class player(entity.entity):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.char = "P"
        
    def tick(self):
        self.move(input("> ")) 
    
    def move(self, direction):
        table = {
         "up":(0,-1),
         "down":(0,1),
         "right":(1,0),       
         "left":(-1,0)
        }
        self.x += table[direction][0]
        self.y += table[direction][1]