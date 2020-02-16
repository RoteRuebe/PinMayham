#!/usr/bin/env python3

import unum
V=unum.Unum.unit("V")
#Ohm=sympy.Symbol("Ohm")
A=unum.Unum.unit("A")

Ohm=(1*V)/(1*A)

#V=1
#A=1

Uq=50*V
Ri=100*Ohm
R1=12000*Ohm
R2=4700*Ohm
R3=6800*Ohm
R4=1200*Ohm
R5=2200*Ohm

R45 = 1/(1/R4+1/R5)
R2345=R2+R3+R45
R12345=1/(1/R1+1/R2345)
Ri12345=Ri+R12345
print ( "R gesamt", Ri12345)
I = Uq / Ri12345
print ( "I gesamt", I )
I1 = R12345 / R1 * I
print ( "I1", I1 )
U1 = R1 * I1
print ( "U1", U1 )
I2 = I - I1
print ( "I2", I2 )
U2 = R2 * I2
print ( "U2", U2 )
I3 = I2
U3 = R3 * I3
print ( "U3", U3 )
I5 = R45 / R5 * I2
print ( "I5", I5 )
I4 = I2 - I5
print ( "I4", I4 )
U4 = I4 * R4
print ( "U4", U4 )
U5 = I5 * R5
print ( "U5", U5 )
print()
print("=======Tests=======" )
print (U1, U4 + U3 + U2 )
print (U4,U5 )
Ui = Ri*I
print (Uq,U4+U3+U2+Ui )
print (Uq,U1+Ui)
