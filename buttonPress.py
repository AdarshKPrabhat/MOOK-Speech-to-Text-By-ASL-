import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setup(26,GPIO.IN,pull_up_down = GPIO.PUD_UP) ##press se input (jo button rasberry pi connected hai)

flag=0

while flag<2:
	inputValue=GPIO.input(26) 

	if inputValue == False and flag == 0:
		print "Microphone  ON "
		flag += 1
		os.system("python audioRecord.py &")
	elif inputValue == False and flag == 1:
		print "Microphone OFF"
		flag += 1
		os.system("pkill -9 -f audioRecord.py") ##killing the file.... off krne ko
		time.sleep(3)

	time.sleep(0.5) ##for flag

GPIO.cleanup()
os.system("python buttonPress.py") ##again 
