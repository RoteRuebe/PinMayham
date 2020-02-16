#!/usr/bin/python
import Pin
#Pin.flag = True
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

    print i
    if i[0] in ["on","off"]:
        for I in i[1:]:
            Pin.pin(I,i[0])
            
    if i[0] in ["blink","welle"]:
        Pin.blink(i[1:],i[0])
            

    if i[0] == "setup":
        print "setup"
        Pin.setup(1)
