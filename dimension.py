from Tkinter import * 
import Tkinter 
import os,sys
from PIL import Image,ImageTk

def something(event):
	event.widget.quit()

root=Tk()
root.bind(something)
root.geometry('%dx%d'%(100,100))
dirlist=os.listdir('/home/pi/Mook/Signs')
old_label_image=None
print dirlist

for f in dirlist:
	f="/home/pi/Mook/Signs/"+f
#	print f
	try:
			
		i1=Image.open(f)
#		print i1
		root.geometry('%dx%d'%(i1.size[0],i1.size[1]))
		Tkpi=ImageTk.PhotoImage(i1)
		print Tkpi
		label_image=Tkinter.Label(root,image=Tkpi)
		label_image.place(x=200,y=2,width=i1.size[0],height=i1.size[1])
		root.title(f)
#		i1.close()
#		if old_label_image is not None:
#			old_label_image.destroy()
		old_label_image=label_image
		root.mainloop()
	except Exception, e:
		print e
		pass
