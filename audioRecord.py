import speech_recognition as sr
import sys
import string
import time
import os
v = " " ##storing text in string.....
print "here"
os.system("sudo rm a.txt")
#loop starts here
while True:
	os.system("sudo rm x.wav x.flac display.txt") ##super user ##remove ##
	os.system("arecord -D plughw:1 -f cd /home/pi/Mook/x.wav -d 5 ") ##start recording and saving to directory
	os.system("ffmpeg -i  x.wav x.flac")

	f=open("a.txt","a+")
	f1=open("display.txt","w")
	r = sr.Recognizer() ##recognising speech recog
	with sr.AudioFile("x.flac") as source: 
		audio = r.record(source) 
#print audio
	try:
     #print("You said " + r.recognize_google(audio))
		v = r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	print v
	f.write(v) #oopar
	f1.write(v)
	f1.close()
	f.close()
	string=v
	os.system("python text.py \"%s\" &"%string)  #new python file for text to correasonding file
#for j in v :
#listofimages=[]
	for i in string:
		i=i.upper()
		if i == " ":
			print "blank"
			os.system("python placing.py bs &")
			time.sleep(2)
			os.system("pkill -9 -f placing") 
		else:
			os.system("python placing.py %s &"%i)
			time.sleep(2)
			os.system("pkill -9 -f placing")
	os.system("pkill -9 -f text")
	time.sleep(50)
