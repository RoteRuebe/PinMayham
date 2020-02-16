#!/usr/bin/python
import sys,os,commands,time,Pin
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#fl = True
#GPIO.setup(7,GPIO.OUT)
#p = GPIO.PWM(7,1)



ping = {
"192.168.0.1":1,
"192.168.0.129":2,
"192.168.0.152":3,
"192.168.0.150":4,
"192.168.0.75":5,
"192.168.0.139":6,
"192.168.0.157":7,
"192.168.0.114":8
}
##"192.168.0.80" = sarah


#Pin.flag = True

while True:
    alive = []
    for key, value in ping.iteritems():
        out = commands.getoutput("fping"+" "+key)
        if "alive" in out:
            out = out.replace("is alive","")
            out = out.strip()
            alive.append(out)



    f = open("Net.txt","w")
    states = Pin.state()
    wstates = []
    for I in states:
        if I == True:
            	wstates.append("True")
        if I == False:            
		wstates.append("False")
    wstates = " ".join(wstates)
    f.write(wstates)
    f.write("\n")
    f.close()
