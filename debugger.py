import ai
import time
import curses
from curses.textpad import rectangle


class viewer:
    def __init__ (self,scr,games):

        curses.curs_set(False)
        self.screen = scr
        self.s_view = curses.newwin(5,9,0,0)
        self.s_select = curses.newwin(7,25,0,15)
        self.screen.refresh()
        rectangle(self.s_view,0,0,4,7)
        self.hi = 0
        self.gi = 0
        self.games = games
        self.draw_select()
        self.draw_board()
        
        while True:
            self.loop()
        
    def loop(self):
        key = self.screen.getch()
        if key == 9:
            self.state += 1
            if self.state >= 2:  self.state = 0
            if self.state < 0:   self.state = 2-1 #len(states) 
            
            
        if key == 260:
            self.hi -= 1
        if key == 261:
            self.hi += 1
            
        if key == 259:
            self.gi -= 1
            self.hi = 0
            self.draw_select()
        if key == 258:
            self.gi += 1
            self.hi = 0
            
        if self.gi < 0:
            self.gi = len(self.games) - 1
            
        elif self.gi >= len(self.games):
            self.gi = 0
            
        self.draw_select()

        if self.hi < 0:
            self.hi = len(self.games[self.gi]._history) - 1
        if self.hi >= len(self.games[self.gi]._history):
            self.hi = 0
            
        self.draw_board()
    
    def draw_board(self):
        for ri, row in enumerate(self.games[self.gi]._history[self.hi]):
            for ci, cell in enumerate(row):
                if cell == 0:
                    a = "X"
                elif cell == 1:
                    a = "O"
                elif cell == 2:
                    a = "-"
                    
                self.s_view.addstr(ri+1,2*ci+1,str(a))
                
        for val in self.games[self.gi]._phistory[self.hi]:
            self.screen.addstr(5,0,str(val))
            break
                
        self.screen.addstr(5,0,str(self.games[self.gi]._phistory[self.hi][self.games[self.gi]._board]))
        
        #[{state:(action:weight)}]
            
        self.s_view.refresh()
        self.screen.refresh()
        
    def draw_select(self):
        self.s_select.clear()
        self.s_select.addstr(0,0,f"{self.games[self.gi].win} game {self.gi}",curses.A_REVERSE)
        self.s_select.refresh()
        
def main(scr):
    A = ai.main()
    viewer(scr,[A.play_round(),A.play_round(),A.play_round()])

curses.wrapper(main)    