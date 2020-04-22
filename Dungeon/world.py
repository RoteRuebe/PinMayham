#!/usr/bin/env python3
import block, copy, random

class world:
    def __init__ (self,screen,width=20,length=10):
        """a world is a container of blocks and entitys, in one isolated space"""
        self._matrix = []
        self.width = width
        self.length = length
        self.entitys = []
        self._screen = screen
        
        row = []
        for _ in range(length):
            for _ in range(width):
                r = random.random()
                if r >= 0.1:
                    row.append(block.earth())
                else:
                    row.append(block.tree())
     
            self._matrix.append(row)
            row = []    
            
    def tick(self):
        """function to cause an in game tick: after any key press,
        every block or entity object's tick function will get called"""
        
        key = self._screen.getkey()
        for ent in self.entitys:
            ent.tick(key)
            
        x,y = 0,0
        for _ in self._matrix:
            for b in _:
                resp = b.tick()
                if "replace" in resp.keys():
                    self._matrix[y].pop(x)
                    self._matrix[y].insert(x,resp["replace"])
                    
                x += 1
            x = 0
            y += 1
            
    def collide_at(self,x,y,you):
        """instance "you" wants to go to x|y. can it? the block at that position
        is politely asked and his answer forwarded to instance "you" """
        if x < 0 or y < 0 or x == self.width or y == self.length:
            return {"walk":False}
        
        return self._matrix[y][x].collision(you)
    
    def get(self,x,y):
        return self._matrix[y][x]
        
    def register_entity(self,new):
        """every freshly spawned entity has to call this function"""
        self.entitys.append(new)
            
    def display (self):
        """function to display the world accordingly"""
        x,y = 0,0
        for row in self._matrix:
            for cell in row:
                    self._screen.addstr(y,x,cell.char) 
                    
                    x += 1
            x = 0
            y += 1
            
        for entity in self.entitys:
            self._screen.addstr(entity.y,entity.x,entity.char)
        
        for entity in self.entitys:
            if entity.name == "player":
                self._screen.addstr(y+3,0,str(entity.inventory))