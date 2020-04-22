#!/usr/bin/env python3
import random, copy

class main:
    def __init__ (self):
        s = [\
        [4,5,0,0,0,0,0,7,8],
        [0,2,0,7,0,3,0,5,0],
        [3,0,0,0,6,0,0,0,2],
        [0,4,0,1,0,9,0,3,0],
        [0,0,8,0,0,0,7,0,0],
        [0,9,0,8,0,5,0,4,0],
        [1,0,0,0,5,0,0,0,4],
        [0,6,0,4,0,2,0,8,0],
        [5,3,0,0,0,0,0,2,7]
        ]
        self.sudo = sudoku(s)
        
    def loop(self):
        for x in range(9):
            for y in range(9):
                if type(self.sudo.get(x,y)) != int or self.sudo.get(x,y) == 0:
                    t = self.test(x,y)
                    if len(t) == 1: t = t[0]
                    self.sudo.ch(x,y,t)
    
    def test(self,x,y):
        poss = [1,2,3,4,5,6,7,8,9]
        for i in self.sudo.line(y):
            if i in poss:  poss.remove(i)
        for i in self.sudo.column(x):
            if i in poss:  poss.remove(i)
        for i in self.sudo.square(int(x/3)+int(y/3)*3):
            if i in poss:   poss.remove(i)
        return poss
    
    def test2(self,what,args):
        out = eval("self.sudo.{}(*{})".format(what,args))
        li = []
        for el in out:
            if type(el) == list:
                for i in el:
                    li.append(i)
        
        s = set(li)   
        for i,e in enumerate(s):
            if li.count(e) > 1:
                while True:
                    try:
                        li.remove(e)
                    except:
                        break
                    
        if len(li) == 1:
            self.sudo.ch()
            
        self.sudo.ch()
    
class sudoku:
    def __init__(self,layout):
        self.l = layout
        
    def ch(self,x,y,l):
        self.l[y][x] = l
        
    def get(self,x,y):
        return self.l[y][x]
    
    def line(self,y):
        return self.l[y]

    def column(self,x):
        f = []
        for i in self.l:
            f.append(i[x])
        return f

    def square(self,n):
        f = []
        ff = []
        x = n % 3
        y =  int(n / 3)
        for i in range(3):
            f.append(self.line(y*3+i))
        for i,e in enumerate(f):
            f[i] = e[x*3:x*3+3]
        for row in f:
            for el in row:
                ff.append(el)
        return ff
       
    def bprint(self):
        for i in self.l:
            for j in i:
                if j != 0 and type(j) != list:
                    print(j,end=" ")
                else:
                    print("_",end=" ")
            print()
        print("\n")
    
m = main()
m.sudo.bprint()
m.loop()
m.test2("square",(5,))
m.sudo.bprint()