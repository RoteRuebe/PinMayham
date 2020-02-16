#!/usr/bin/python
import Pins,time,sys
def Write(z):
    for I in z:
        if I == True:
            print "*",
        if I == False:
            print "O",
    print ""

def Input(x):
    for I,J in zip(x,range(len(x))):
        J += 1
        I = int(I)
        if I == 1:
            Pins.pin(J+4+(4-len(x)),"on")
            #print J,len(x) 
                
        if I == 0:
            print "OFF"
            Pins.pin(J+4+(4-len(x)),"off")
            #print J,len(x)
        if J == 4:
            z = Pins.pin("all","states")
            Write(z)
            
    return(x)

def BinToDez(num):
    fn = 0
    for I,J in zip(num,range(4,0,-1)):
        fn += int(I)*2**(J-1)
    return(fn)

                
print "Enter first Digit"
f = Input(raw_input(":"))
cf = BinToDez(f)    
print cf
    
print "Enter second Digit"
s = Input(raw_input(":"))
cs = BinToDez(s)
print cs
print "Calculating...."
x = bin(cf+cs)
x = x[2:]
print x
Input(x)