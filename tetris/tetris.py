#!/usr/bin/python3
import curses, time, keyboard, random
from data import *

class map:
    def __init__ (self):
        self.tetris = tetris(self) 
        self.map = []
        for _ in range(20): self.map.append([0,0,0,0,0,0,0,0,0,0])

    def beat(self):
        self.do_inp()

        if self.tetris.check(offset_y=1):
            for y in range(len(self.tetris.blockmap)):
                for x in range(len(self.tetris.blockmap[0])):
                    self.map[y+self.tetris.offset[1]][x+self.tetris.offset[0]] = self.tetris.blockmap[y][x]
            self.tetris.start_over()
        else:
            self.tetris.offset[1] += 1

    def do_inp(self):
        l = []
        if keyboard.is_pressed("a") and not self.tetris.check(offset_x=-1):   self.tetris.offset[0] -= 1
        if keyboard.is_pressed("d") and not self.tetris.check(offset_x=1):     self.tetris.offset[0] += 1
        if keyboard.is_pressed("q"):   self.tetris.turn()

    def get(self,x,y):
        if len(self.map)-1 >= y and len(self.map[0])-1 >= x and x >= 0 and y >= 0:
            return self.map[y][x]
        else:
            return 1

class tetris:
    def __init__ (self,world):
        self.world = world
        self.offset = [1,1]
        self.blockmap = []
        self.turnmaps = []
        self.i = 0
        self.start_over()

    def check(self,offset_x=0,offset_y=0):
        x,y = [0,0]
        for row in self.blockmap:
            for block in row:
                if block:
                    if self.world.get(self.offset[0]+x+offset_x, self.offset[1]+y+offset_y):
                        return 1
                x += 1
            x = 0
            y += 1

        else:
            return 0

    def turn(self):
        self.i += 1
        if self.i > len(self.turnmaps)-1:  self.i = 0 
        self.blockmap = self.turnmaps[self.i]

    def start_over(self):
        self.offset = [0,0]
        self.turnmaps = random.choice(data)
        self.blockmap = self.turnmaps[0]

@curses.wrapper
def main(screen):
    curses.curs_set(0)
    w = map()
    while True:
        x,y = [0,0]
        for row in w.map:
            for cell in row:
                if cell:
                    screen.addstr(y,x,"  ",curses.A_REVERSE)
                else:
                    screen.addstr(y,x,"  ")

                x += 2
            x = 0 
            y += 1
        
        x,y = [0,0]
        for row in w.tetris.blockmap:
            for cell in row:
                if cell:
                    screen.addstr(y+w.tetris.offset[1],x+w.tetris.offset[0]*2,"  ",curses.A_REVERSE)
                else:
                    screen.addstr(y+w.tetris.offset[1],x+w.tetris.offset[0]*2,"  ")

                x += 2
            x = 0 
            y += 1

        screen.refresh()
        w.beat()
        time.sleep(0.1)
