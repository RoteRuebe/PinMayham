#!/usr/bin/env python3
class entity:
    def __init__(self,char,x,y):
        self.x = x
        self.y = y
        self.char = char
    
    def tick(self):
        pass
    
    def display(self):
        print(self.char,end="")
        