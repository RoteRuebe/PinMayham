#!/usr/bin/env python3
class block:
    def __init__ (self,char):
        self.char = char
        
    def display(self):
        print(self.char,end="")
        
    def interaction(self,other):
        pass
        
class tree(block):
    def __init__ (self):
        self.char = "T"
        
class earth(block):
    def __init__ (self):
        self.char = "e"