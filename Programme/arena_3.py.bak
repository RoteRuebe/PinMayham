import numpy
from collections import OrderedDict
import os

class unit:
    '''The class which represents one electoral unit.'''
    def __init__ ( self, num_voters, parties_1, parties_2, transition ):
        self.votes1 = self.get_votes1( num_voters, parties_1 )
        self.transition = self.simulate_transition( transition )
        self.votes2 = self.get_votes2( parties_2 )
    
    def get_votes1( self, voters, parties ):
        '''The function that generates the results of the first ballot.'''
        list = OrderedDict()
        for I in parties:
            value = numpy.random.poisson(voters * numpy.random.normal(1,0.2) * parties[I])
            list.update( {I:int(round(value))})
        return list
    
    def simulate_transition ( self, transition ):
        '''The function that generates the transition of voters.''' 
        final_transition = []
        for I in range(len(transition)):
            final_transition.append( list( numpy.random.multinomial( self.votes1.values()[I], transition[I] )))
        return final_transition
        
    def get_votes2 ( self, parties ):
        '''The function that calculates the results of the second ballot.'''
        list = OrderedDict()
        for I in range(len(parties)):
            value = 0
            for J in range(len(self.transition)):
                value += self.transition[J][I]
            
            list.update( {parties[I]:int(round(value))})
            
        return list
    
class election:
    '''The class which represents one electoral event.'''
    def __init__ ( self, unit_num, voters, parties_1, parties_2, transition ):
        self.units = self.gen_units( unit_num, voters, parties_1, parties_2, transition )
                                
    def gen_units( self, unit_num, voters, parties_1, parties_2, transition ):
        '''The function that generates the 'unit' classes.'''
        list = []
        for I in range(unit_num):
            list.append( unit( voters, parties_1, parties_2, transition) )
        return list