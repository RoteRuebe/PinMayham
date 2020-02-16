#!/usr/bin/python

flag = True
import sys
if len(sys.argv)>1:
    flag=True

if flag == False:
    import RPi.GPIO as GPIO
import time
import atexit


def yannicksExitFunction():
    for I in pins.keys():
        pin(I,"off")
        

atexit.register ( yannicksExitFunction )

if flag == False:
    GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)

states = [False]*8

pins = {
1:4,
2:17,
3:18,
4:27,
5:22,
6:23,
7:24,
8:25
}

rpins = {}
for k,v in pins.items():
    rpins[v]=k
    
if flag == False:
    for I in pins.items():
        GPIO.setup(I,GPIO.OUT)



print pins




def pin (num,action):
    if action == "on":
        if flag == False:
            GPIO.output(pins[num],GPIO.HIGH)
        else:
            states[num-1] = True
        
    elif action == "off":
        if flag == False:
            GPIO.output(pins[num],GPIO.LOW)
        else:
            states[num-1] = False
            
    elif action == "states":
        if num == "all":
            return(states)
        else:
            return(states[num])
    
    #if flag:
        #return(states)
        
        
def blink(num,action):
    if action == "blink":
        for x in range(10):
            for I in num:
                pin(I,"on")
            time.sleep(0.5)
            
            for I in num:
                pin(I,"off")
                
            time.sleep(0.5)
            
    if action == "welle":
        for I in range(5):
            a = 1
            b = 3
            pin(1,"on")
            time.sleep(0.1)
            pin(2,"on")
            for I in range(6):
                time.sleep(0.1)
                pin(a,"off")
                pin(b,"on")
                a += 1
                b += 1
            time.sleep(0.1)
            pin(7,"off")
            time.sleep(0.1)
            pin(8,"off")
            time.sleep(0.1)
            pin(8,"on")
            time.sleep(0.1)
            pin(7,"on")
            time.sleep(0.1)
            c = 8
            d = 6
            for I in range(6):
                pin(c,"off")
                pin(d,"on")
                c -= 1
                d -= 1
                time.sleep(0.1)
                
            pin(2,"off")
            time.sleep(0.1)
            pin(1,"off")
            time.sleep(0.1)
        
def setup(pin):
    print "Is this pin number",pin,"?"
    pin(pin,"on")
    time.sleep(0.5)
    pin(pin,"off")
    if raw_input("(y/n):") == "y":
        print "Setup complete!"
        
    else:
        setup(pin+1)

        

