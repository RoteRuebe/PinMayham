#!/usr/bin/python
import sys,os,Pin,commands,time
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
fl = True
GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,1)


ping = {
1:










}



while True:
	c = True
	x = commands.getoutput("fping -g 192.168.0.0/24 2<&1 | grep alive").split("is alive")
	for c,I in enumerate(x):
		x[c]=I.strip()
	x.remove("")

	with open("Net.txt","rt") as f:
		f.write("Helo")

	for I in range(1,9):
		Pin.pin(I,"off")


	g = commands.getoutput("fping google.com")
	if "alive" in g:
		Pin.pin(10,"on")
		p.start(0)
		fl = True
	
	else:	
		for I in range(1,12):
			Pin.pin(I,"off")
			fl = False
		p.start(50)
		while c:
			time.sleep(10)
			if "alive" in commands.getoutput("fping google.com"):
				c = False




	for I in x:
		if fl:
			if I == "192.168.0.1":
				Pin.pin(1,"on")
				#print "gateway online"
			#else:
				#print "gateway is offline"

			if I == "192.168.0.129":
				Pin.pin(2,"on")
				#print "Higgs online"
			#else:
				#print "Higgs off"

			if I == "192.168.0.152":
				Pin.pin(3,"on")
				#print "Saphire online"

			#else:
				#print "Saphire off"

			if I == "192.168.0.150":
				Pin.pin(4,"on")
				#print "Hila is on"
			#else:
				#print "Hila off"
				
			if I == "192.168.0.75":
				Pin.pin(5,"on")
				#print "Waldi is on"

			#else:
				#print "Waldi off"

			if I == "192.168.0.139":
				Pin.pin(6,"on")
				#print "Yannick is on"

			#else:
				#print "Yannick off"

			if I == "192.168.0.157":
				Pin.pin(7,"on")
				#print "Pavillion on"
			#else:
				#print "Pavillion off"

			if I == "192.168.0.114":
				Pin.pin(8,"on")
				#print "Hilas Ipad online"

			#else:
				#print "Hilas Ipad off"
		
			if I == "192.168.0.80":
				print "JAYWUHU"
				Pin.pin(11,"on")
	time.sleep(120)
