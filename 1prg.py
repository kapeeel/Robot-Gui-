from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from PIL import ImageTk, Image
from image_to_gcode import *



x=Tk()
x.title("BeeClust")
fra=Frame(x, width=50000, height=50000)
fa=Frame(x)

def destroy(a) :
	a.destroy()
	



def opnimg () :	
	filename = tkFileDialog.askopenfilename(parent=x, initialdir = "",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("all files","*.*")))
	img=ImageTk.PhotoImage(Image.open(filename))
	k=Label(fa, image=img)
	k.pack(fill="both", expand="yes")
	destroy(img)
	kap=ImageToGcode()
	#filename.destroy()
	
	testfile='1file'+'.txt'
	in_file=open(testfile,'w')
	in_file.write(__init__(img))

	k.mainloop()

	k.pack_forget()
	img.pack_froget()


b1=Button(fra, text="Open", command=opnimg, fg="Black", 
	bg="White", width=15)
fa.pack_forget()
b2=Button(fra, text="Quit", command=x.quit, fg="Black", bg="White", width=15)
b1.pack(side="left")
b2.pack(side="right")
fra.pack(side="bottom")
fa.pack(side="top")
x.mainloop()
