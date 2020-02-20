#!/usr/bin/env python3
import copy,random,pygame,time
class game:
    def __init__ (self,players):
        self.players = players
        self.dice = [0,0]
        self.loop()
        
    def loop(self):
        while True:
            self.roll_dice()
            for player in self.players:
                player.turn(self.dice)
        
        
    def roll_dice(self):
        self.dice[0] = int(random.uniform(1,6))
        self.dice[1] = int(random.uniform(1,6))

class board:
    def __init__ (self,name=""):
        #initalize a 5*5 2d array with cell object s
        row = []
        self.map = []
        
        self.combos = {}
        
        for I in range(5):
            row.append(cell())
            
        for I in range(5):
            self.map.append(copy.deepcopy(row))
        
        #set constants init sound
        self.offset  =  50
        self.sound_write = pygame.mixer.Sound("write.wav")
        self.sound_error = pygame.mixer.Sound("error.wav")
        
        self.dice = None
        self.name = name
        
        #initialize screen  
        self.dice_img = []
        for I in range(1,7):
            self.dice_img.append(pygame.transform.scale(pygame.image.load("würfel"+str(I)+".jpg"),(50,50)))
            
        self.screen = pygame.display.set_mode((410,410))
        self.screen_game = self.screen.subsurface(pygame.Rect(80,80,self.offset*5,self.offset*5))
        self.font = pygame.font.SysFont("Comic Sans MS",50)
   
    def do(self,x,y,display=True):
        if display:
            self.display()
        
        if self.combos == {}:
            what = self.do_num(x,y,sum(self.dice))
            if what == "write":
                out = self.get_combos(x,y)
                for I, sout in zip( (y,x,0,0),out.keys() ):
                    if (sout,I) in self.combos:
                        self.combos[sout,I] += out[sout]
                    elif out[sout] != 0:
                        print(out[sout])
                        self.combos[(sout,I)] = out[sout] 
        else:
           self.exec_combo(x,y)
        
    def get_combos(self,x,y):
        #search for combos
        a = self.get_list("row",y)
        b = self.get_list("column",x)
        if x == y:
            c = self.get_list("quer1")
        else:
            c = [None]*5
        if x + y == 4:
            d = self.get_list("quer2")
        else:
            d = [None]*5

        a = self.check_for_combos_in_list(a)
        b = self.check_for_combos_in_list(b)
        c = self.check_for_combos_in_list(c)
        d = self.check_for_combos_in_list(d)
        
        return {"row":a,"column":b,"quer1":c,"quer2":d}
        
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
    def get_list(self,which,cor=None,get_int=True):
        fin = []
        if which == "row":
            for cell in self.map[cor]:
                if get_int:
                    fin.append(cell.num)
                else:
                    fin.append(cell)
                    
        elif which == "column":
            for row in self.map:
                if get_int:
                    fin.append(row[cor].num)
                else:
                    fin.append(row[cor])
        
        elif which == "quer1":
            for I in range(5):
                if get_int:
                    fin.append(self.map[I][I].num)
                else:
                    fin.append(self.map[I][I])

        elif which == "quer2":
            for I in range(5):
                if get_int:
                    fin.append(self.map[I][4-I].num)
                else:
                    fin.append(self.map[I][4-I])
        
        return fin
    
    def check_for_combos_in_list(self,list):
        #check for certain combos in list and return, how many circles that is worth
        if None in list:
            return 0
        
        for I in range(2,13):
            if list.count(I) == 5:
                return 3
            if list.count(I) == 4:
                return 2
            if list.count(I) == 3:
                for J in range(2,13):
                    if list.count(J) == 2 and J != I:
                        return 2
                return 1
            
            if list.count(I) == 2:
                print(I)
                for J in range(2,13):
                    if list.count(J) == 2 and J != I:
                        print(J)
                        return 1
            
        list.sort()
        for I in range(4):
            if list[I]+1 != list[I+1]:
                return 0
        return 3
            
    def exec_combo(self,x,y):
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        for key in self.combos.keys():
            if not self.get(x,y,"circle"):
                if key[0] == "row":
                    if key[1] == y:
                        self.circle(x,y)
                        self.combos[("row",y)] -= 1
                
                elif key[0] == "column":
                    if key[1] == x:
                        self.circle(x,y)
                        self.combos[("column",x)] -= 1
                    
                elif key[0] == "quer1":
                    if x == y:
                        self.circle(x,y)
                        self.combos[("quer1",0)] -= 1
                    
                elif key[0] == "quer2":
                    if x + y == 4:
                        self.circle(x,y)
                        self.combos[("quer2",0)] -= 1
                
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        self.cleanup_combos()
                        
    def cleanup_combos(self):
        clean = []
        for key, value in self.combos.items():
            if value == 0:
                clean.append(key)
                
            l = self.get_list(key[0],key[1],False)
            for index,I in enumerate(l):
                l[index] = I.hasCircle
                
            if l == [True]*5:
                clean.append(key)
                
        for I in clean:
            self.combos.pop(I)
            
            
    def display (self):
        #draw to the pygame display
        #reset screen
        self.screen.fill((0,0,0))
        #draw meta-information
        dice1 = self.dice_img[self.dice[0]-1]
        dice2 = self.dice_img[self.dice[1]-1]
        self.screen.blit(dice1,(0,0))
        self.screen.blit(dice2,(50,0))
        name = self.font.render(self.name,True,(255,255,255))
        self.screen.blit(name,(205-name.get_width()/2,0))
        
        
        #draw numbers
        x = 0
        y = 0
        for row in self.map:
            for cell in row:
                if cell.num:
                    self.draw_num(x,y,cell.num,cell.hasCircle)
                x += 1
            x = 0
            y += 1
            
        #draw the horizontal lines
        x = 50
        for I in range(5):
            line = pygame.Rect(x,0,3 ,self.offset*5)
            self.screen_game.fill((128,128,128),line)
            x += self.offset
            
        #draw the vertical lines    
        y = 50
        for I in range(5):
            line = pygame.Rect(0,y,self.offset*5 ,3)
            self.screen_game.fill((128,128,128),line)
            y += self.offset
        
        pygame.display.flip()

        
    def draw_num(self,x,y,num,circle):
        #draw a number at pos(x|y)
        x *= self.offset
        y *= self.offset
        
        if circle:
            textsurface = self.font.render("("+str(num)+")", True, (255, 255, 255))
        else:
            textsurface = self.font.render(str(num), True, (255, 255, 255))
        x += self.offset/2 - textsurface.get_width()/2
        y += self.offset/2 - textsurface.get_height()/2
        self.screen_game.blit(textsurface,(x,y))
        pygame.display.flip()
        
    def get_mouse(self):
        #wait for mouse input and return (x|y) of mouse
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x = event.pos[0]
                        y = event.pos[1]
                        x -= self.screen_game.get_offset()[0]
                        y -= self.screen_game.get_offset()[1]
                        x = int(x/self.offset)
                        y = int(y/self.offset)
                        return x,y
                    
    def in_combos(self,key):
        for I in self.combos:
            if key == I:
                return True
        return False
    
    def get_in_combos(self,key):
        for I in self.combos:
            if key == I:
                return I
        return None
            
    def do_num(self,x,y,num):
        return self.map[y][x].do_num(num)
        
    def circle(self,x,y):
        return self.map[y][x].circle()
    
    def get(self,x,y,mode="num"):
        if mode == "num":
            return self.map[y][x].num
        if mode == "circle":
            return self.map[y][x].hasCircle
        else:
            return self.map[y][x]
    
class cell:
    def __init__ (self):
        self.num = None
        self.hasCircle = False
        
    def do_num(self,num):
        #checks if it has to cirlce/write num and does so
        if self.num == None:    
            self.write(num)
            return "write"
    
        elif not self.hasCircle and num == self.num:    
            self.hasCircle = True
            return "circle"
        
        else:   
            return None
        
    def write (self,num):
        if type(num) == int and 2 <= num <= 12:
            self.num = int(num)
            return "write"
        
        else:   
            return None
        
    def circle(self):
        if self.num:
            self.hasCircle = True
            return "circle"
        
        else:   
            return None
        

class player:
    def __init__ (self,name=""):
        self.name = name
        self.board = board()
        
    def turn(self,dice):
        self.board.dice = dice
        self.board.display()
        x,y = self.board.get_mouse()
        self.board.do(x,y)
                
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
            
g = game( [player("yannick")] )
