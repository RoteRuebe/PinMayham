import pickle, numpy
from waehlerstromrechner_2 import *
from simulation_3 import *
from arena_3 import *

class reader:
    def __init__ ( self, file ):
        '''The class which enables the user to use and interprete the results of the simulation.py file.'''
        self.file = file
        
        ## (1) Loading the data
        
        f = open(file,"r")
        self.input = pickle.load(f)
        f.close()
        
        ## (2) Space for special inquerries
        
        #...
    
    def average_error ( self ):
        sum = 0
        for I in self.input:
            sum += self.measure_error(I)
        return sum / len(self.input)
        
                
    def measure_error ( self, input ):
        real_transition = self.unchain( self.formalize_matrix( self.measure_real_transition( input ) ) )
        projection = numpy.matrix( self.measure_projected_transition( input ) )
        
        dif = ( numpy.add(numpy.dot(-1,real_transition), projection ) )
        
        return numpy.dot( dif, dif.T )
        
    def measure_projected_transition ( self, input ):
        return input.voters_transition.data_output
            
    def measure_real_transition ( self, input ):
        list = input.units[0].transition
        for I in input.units[:]:
            list = numpy.add( list, numpy.matrix( I.transition ))
        return list
        
    def formalize_matrix ( self, matrix ):
        list = numpy.asarray(matrix)
        new_list = []
        for row in list:
            new_row = []
            sum = 0
            for cell in row:
                sum += cell
            for cell in row:
                new_row.append( float(cell) / float(sum) )
            new_list.append(new_row)
        return numpy.matrix(new_list)
    
    def unchain ( self, matrix ):
        list = []
        array = numpy.asarray(matrix)
        for row in array:
            for cell in row:
                list.append(cell)
        return numpy.matrix(list)
    
r = reader("file.txt")
print r.average_error()