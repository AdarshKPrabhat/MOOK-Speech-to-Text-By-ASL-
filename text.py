import Tkinter as tk
from  PIL import Image,ImageTk
import argparse
import time
parser=argparse.ArgumentParser()
parser.add_argument("text")
args=parser.parse_args()
name=str(args.text)
print name
root=tk.Tk()
w=1000
h=100
x=400
y=600
root.title("fim")
#path="/home/pi/Mook/Signs/%s.jpg"%name
#img=ImageTk.PhotoImage(Image.open(path))
root.geometry('%dx%d+%d+%d' %(w,h,x,y))
label=tk.Label(None,text=name)
label.pack()
root.mainloop()




