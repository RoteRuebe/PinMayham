#!/usr/bin/python
import Pin,time
def DisplayNet():
	f = open("Net.txt","r")
	states = f.read().split(" ")
	f.close()
	for I in range(1,8):
		states[I].strip()

	for I,J in enumerate(states):
        	if J == "True":
            		Pin.pin(I+1,"on")
          
		if J == "False":
			Pin.pin(I+1,"off")
            
def off():
	for I in range(1,8):
		Pin.pin(I,"off")

while True:
	off()
	DisplayNet()
	time.sleep(10)

