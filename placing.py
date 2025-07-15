import Tkinter as tk
from  PIL import Image,ImageTk
import os
import argparse
import time
parser=argparse.ArgumentParser()
parser.add_argument("image")
args=parser.parse_args()
name=args.image
#os.system("python placing1.py &")
root=tk.Tk()
w=500
h=500
x=700
y=50
root.title("fim")
path="/home/pi/Mook/Signs/%s.jpg"%name
img=ImageTk.PhotoImage(Image.open(path))
root.geometry('%dx%d+%d+%d' %(w,h,x,y))
label=tk.Label(root,image=img)
#print "here"
label.pack(side="bottom",fill="both",expand="yes")
print "here"
#time.sleep(3)
#os.system("pkill -9 -f placing")
root.mainloop()
#time.sleep(3)
#os.system("pkill -9 -f fim")



