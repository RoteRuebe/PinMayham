#!/usr/bin/python3
import numpy.random
import random, time, sys, copy

class main:
    def __init__ (self):
        self.win1 = 0
        self.win2 = 0
        self.tie = 0
        self.game = game()
        self.p1 = actor(1,self.game)
        self.p2 = actor(2,self.game)
        
    def play_round(self):
        result = self.game.play()
        if result == 1:
            self.win1 += 1
            self.p1.end(1)
            self.p2.end(0)
            
        elif result == 2:
            self.win2 += 1
            self.p1.end(0)
            self.p2.end(1)
        
        elif result == 3:
            self.tie += 1
            self.p1.end(2)
            self.p2.end(2)
            
        self.game.end()
        
            
        return result
            

class game:
    def __init__ (self):
        self._data = []
        self._n = 0
        self.mode = 0
        self.players = []
        for i in range(3):  self._data.append([0,0,0])
        
    def play(self):
        while True:
            self.act( 1,self.players[0].act() )
            a = self.check_end()
            if a != False:
                break
            
            self.act( 2,self.players[1].act() )
            a = self.check_end()
            if a != False:
                break
            
        

    def act(self, you, crd):
        if you in [1,2]:
            if self._data[crd[0]][crd[1]] == 0:
                self._n += 1
                self._data[crd[0]][crd[1]] = you
            
            else:
                raise Exception("ahhhh what tha fuck")

        return self.check_end()

    def check_end(self):
        for p in [1,2]:
            for i in range(3):
                #rows
                if self.get_state()[i] == (p,p,p):
                    return p
                
                #columns
                if [self.get_state()[j][i] for j in range(3)] == [p,p,p]:
                    return p

           #diagonals
            if [self.get_state()[j][j] for j in range(3)] == [p,p,p]:
                return p

            if [self.get_state()[j][2-j] for j in range(3)] == [p,p,p]:
                return p

        if self._n == 9:
            return 3

        return False

    def end(self):
        self._data = []
        for i in range(3):  self._data.append([0,0,0])
        self._n = 0
        
        
    def get_actions(self):
        i = []
        for r,row in enumerate(self._data):
            for c,cell in enumerate(row):
                if cell == 0:
                    i.append([r,c])
        return i

    def get_state(self,you):
        you = self.players.index[you]
        fin = []
        for row in self._data:
            rrow = copy.deepcopy(row)
            if you == 2:
                for cell in row:
                    if cell == 2:
                        rrow.append(1)
                    if cell == 1:
                        rrow.append(2)
                    if cell == 0:
                        rrow.append(0)
                        
            fin.append(tuple(rrow))
                    
        return tuple(fin)


class actor():
    def __init__ (self,game):
        self.game = game
        self.policy = {
            #state: { action: weight, },
        }

        self.game_history = {
            #state:action,
        }
        self.r = 0.75

    def act(self):
        state = self.game.get_state(self.who)

        if state not in list(self.policy.keys()):
            pa = self.game.get_actions()
            nac = {}
            for x in pa:
                nac[tuple(x)] = 1/len(pa)

            self.policy[state] = nac

        if random.random() >= self.r:
            #non-random move
            actions, weights = [],[]
            for k,v in self.policy[state].items():
                actions.append(k)
                weights.append(v)
            action = numpy.random.choice(a=actions+["a"],p=weights+[0],replace=False)
                                                  #workaround for bug with function
        else:
            #random move
            action = random.choice(self.game.get_actions())

        self.game_history[state] = tuple(action)
        return action
    

    def end(self,x):
        if x == 0:
            for state,action in self.game_history.items():
                self.policy[state][action] -= 0.1

                if self.policy[state][action] < 0:
                    self.policy[state][action] = 0

        elif x == 1:
            for state,action in self.game_history.items():
                self.policy[state][action] += 0.1

        elif x == 2:
            pass

        if x != 2:
            for state,v in self.policy.items():
                s = 0
                for action, weight in v.items():
                    s += weight
            
                for action, weight in v.items():
                    self.policy[state][action] = self.policy[state][action] / s

        self.game_history = {}
        self.r *= 0.9

a = main()

while True:
    a.play_round()
    if (a.tie + a.win1 + a.win2) % 100 == 0:
        print("""
______________________
   {} games played
Player 1 won {} times
Player 2 won {} times
There were   {} ties
______________________
""".format(a.tie+a.win1+a.win2,a.win1,a.win2,a.tie))
        if a.tie == 100 or a.win1 == 100:
            a.p1.policy = {}
            a.p1.r = 0.75
            
            a.p2.policy = {}
            a.p2.r = 0.75
            
        a.tie, a.win1, a.win2 = 0,0,0
        
        #a.game.players = a.game.players[1],a.game.players[0]
        
        #a.p1.who = 1 if a.p1.who == 2 else 2
        #a.p2.who = 1 if a.p2.who == 2 else 2
    
    


