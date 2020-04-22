#!/usr/bin/env python3
class entity:
    def __init__(self,name,char,x,y,world):
        """an enitity represents something, that is able to
        move and interact with the world."""
        self.name = name
        self.x = x
        self.y = y
        self.world = world
        self.char = char
        world.register_entity(self)
    
    def tick(self):
        """this function gets called every unit of time in the game"""
        pass
    
    def move(self,x,y):
        """tries to move self to pos x y"""
        resp = self.world.collide_at(x,y,self)
        if resp["walk"]:
            self.x = x
            self.y = y
            
        return resp
        
        
class player(entity):
    def __init__ (self,x,y,world):
        entity.__init__(self,"player","P",x,y,world)
        self.inventory = []
        self._mode = "move"
        
    def tick(self,key):     
        #change mode or act according to it
        if key == "i":
            self._mode = "interact"
            
        elif key == "b":
            self._mode = "build"

    
        elif key in ["w","a","s","d"] and self._mode != "walk":
            table = {
             "w":(0,-1),
             "s":(0,1),
             "d":(1,0),       
             "a":(-1,0)
            }
            x = self.x + table[key][0]
            y = self.y + table[key][1]
            exec("self.{}(x,y)".format(self._mode))
            
            self._mode = "move"
        
    def interact(self,x,y):
        get = self.world.get(x,y)
        if get.name == "tree":
            resp = get.interact("chop")
            for drop in resp["drops"]:
                self.inventory.append(drop)
            
    def build(self,x,y): 
        pass     
    