#!/usr/bin/python2
OUT,BCM = "",""
HIGH,LOW = "*","O"
lamps = {}
def setup(num,mode):
    if mode == OUT:
        return
    else:
        raise Exception("Emulator only emulates Output mode")

def setmode(mode):
    return

def setwarnings(x):
    return
        
def output(pin,what):
    if pin not in lamps:
        lamps[pin] = HIGH
    if what == HIGH:
        lamps[pin] = HIGH
    elif what == LOW:
        lamps[pin] = LOW
    display()
        
def display():
    for item,key in lamps.items():
        print key,
    print