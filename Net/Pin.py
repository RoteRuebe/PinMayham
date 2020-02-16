#!/usr/bin/python
C = [0]
flag = False
import sys 
if len(sys.argv)>1: 
	flag=True
if flag == False:
	import RPi.GPIO as GPIO
import time
import atexit


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
8:25,
"red":7,
"green":8,
11:11
}

def yannicksExitFunction():
	for I in pins.keys():
		pin(I,"off")


atexit.register ( yannicksExitFunction )

if flag:
	for I in pins.keys():
		if type(I) != int or I > 8:
			pins.pop(I)

rpins = {}
for k,v in pins.items():
	rpins[v]=k
	
if flag == False:
	for I in pins.values():
		GPIO.setup(I,GPIO.OUT)



#print pins




def pin (num,action):
	if type(num) == list:
		for I in num:
			pin(I,action)
		return
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
	
	"""
	if flag:
		for I in states:
			if I == True:
				print "*",
				
			elif I == False:
				print "O",
		print ""
	"""
		#sys.stdout.write(u"\u001b[1A")
		
		
def blink(num,action,sleep=1,times=1):
	if type(num) != list:
		blink([num],action,sleep,times)
		return
	if action == "blink":
		for x in range(times):
			for I in num:
				pin(I,"on")
			time.sleep(sleep)
			
			for I in num:
				pin(I,"off")
				
			time.sleep(sleep)
			
	if action == "welle":
		print "welle"
		for I in range(times):
			a = 1
			b = 3
			print "1,on"
			pin(1,"on")
			time.sleep(sleep/10)
			pin(2,"on")
			for I in range(6):
				time.sleep(sleep/10)
				pin(a,"off")
				pin(b,"on")
				a += 1
				b += 1
			time.sleep(sleep/10)
			pin(7,"off")
			time.sleep(sleep/10)
			pin(8,"off")
			time.Truesleep(sleep/10)
			pin(8,"on")
			time.sleep(sleep/10)
			pin(7,"on")
			time.sleep(sleep/10)
			c = 8
			d = 6
			for I in range(6):
				pin(c,"off")
				pin(d,"on")
				c -= 1
				d -= 1
				time.sleep(sleep/10)
				
			pin(2,"off")
			time.sleep(sleep/10)
			pin(1,"off")
			time.sleep(sleep/10)

def setup(num,first=True):
	if first:
		C[0] = num
	print C[0]
	print "Is this pin number",C[0],"?"
	pin(num,"on")
	time.sleep(1)
	pin(num,"off")
	if raw_input("(y/n):") == "y":
		print "Setup complete!"
		
	else:
		setup(num+1,False)

		
		
def state():
	return(states)

"""
while True:
	print ""
	i = raw_input(":")
	
		
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
		
	if i[0] in ["on","off"]:
		for I in i[1:]:
			pin(I,i[0])
			
	if i[0] in ["blink","welle"]:
		blink(i[1:],i[0])
			

pin(1,"blink")
"""
