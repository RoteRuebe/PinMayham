#!/usr/bin/env python3
import random
class block:
    def __init__ (self,name,char,walkable):
        """a block represents one tile on the map."""
        self.name = name
        self.char = char
        self.walkable = walkable
        
    def tick(self):
        """this function gets called every unit of time.
        you may return certain requests. 
        
        Replace yourself with another object by returning
        {"replace":<new instance>} """
        
        return {}
    
    def interact(self,how):
        """this function gets called if this object is being interacted with.
        "how" determines how it is being interacted with"""
        
        return {"error":"interactions are not specified"}
        
    def collision(self,other):
        """this function gets called, when an entity is colliding with this object
        a variable "walkable" is defined, so subclasses dont have to overwrite this
        function just to define if one can walk on this block"""
        
        if self.walkable:
            return {"walk":True}
        
        else:
            return {"walk":False}
        
class tree(block):
    def __init__ (self):
        block.__init__(self,"tree","T",False)
        self._choped = False
        
    def interact(self,how):
        if how == "chop":
            self._choped = True
            return {"drops":("log",)*int(random.uniform(1,3))}
        
        return {"error":"unknown interaction"}
            
    def tick(self):
        if self._choped:
            return  {"replace":earth()}
        else:
            return {}
        
class earth(block):
    def __init__ (self):
        block.__init__(self,"earth","e",True)
        
    def tick(self):
        r = random.random()
        if r < 0.01:
            return {"replace":grass()}
            
        return {}

class grass(block):
    def __init__ (self):
        block.__init__(self,"grass","g",True)
        