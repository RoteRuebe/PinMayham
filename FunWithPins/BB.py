#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import atexit


def yannicksExitFunction():
    for I in pins.keys():
        pin(I,"off")
        

atexit.register ( yannicksExitFunction )


GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)
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
for I in pins.items():
    GPIO.setup(I,GPIO.OUT)



print pins




def pin (num,action):
    if action == "on":
        GPIO.output(pins[num],GPIO.HIGH)
    
    elif action == "off":
        GPIO.output(pins[num],GPIO.LOW)
        
    elif action == "blink": a
        for I in range(10):
            pin(num,"on")
            time.sleep(1)
            pin(num,"off")
            time.sleep(1)
        
        
        
def setup(pin):
    print "Is this pin number",pin,"?"
    pin(pin,"on")
    time.sleep(0.5)
    pin(pin,"off")
    if raw_input("(y/n):") == "y":
        print "Setup complete!"
        
    else:
        setup(pin+1)

        

while True:
    try:
        i = raw_input(":")
    except:
        print "What?"
        continue
        
    i = i.replace("all","1 2 3 4 5 6 7 8")
    i = i.split(" ")
    try:
        for ctr in range(1,len(i)):
            if ctr == 1:
                if i[1] == "all":
                    continue
            i[ctr]=int(i[ctr])
    except:
        print "Not a valid input"
        
    if i[0] in ["on","off","blink"]:
        for I in i[1:]:
            pin(I,i[0])


