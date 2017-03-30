from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from PIL import ImageTk, Image
from image_to_gcode import *

x=Tk()
x.title("BeeClust")
Bframe=Frame(x)  #Button's Frame
#Iframe=Frame(x)  #Image's Frame

class image:
	def __init__(self, master) :
		self.b1=Button(Bframe, text="Open", command=self.dispimg, fg="Black", bg="White", width=15)
		self.b2=Button(Bframe, text="Quit", command=x.quit, fg="Black", bg="White", width=15)
		self.b1.pack(side="left")
		self.b2.pack(side="right")	





	def dispimg(self) :	
		self.Iframe=Frame(x)
		self.filename = tkFileDialog.askopenfilename(parent=x, initialdir = "",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("all files","*.*"))) #selecting image file
		self.img=ImageTk.PhotoImage(Image.open(self.filename)) #opening imagefile
		self.i1=Label(Iframe, image=self.img)
		self.i1.pack(fill="both", expand="yes")
		Iframe.pack(side="top")
		self.i1.mainloop()
		self.destroy(self.Iframe)
		#self.img.destroy()

	def destroy(a) :	
		a.destroy()


kapil=image(x)	
kothari=ImageToGcode(kapil)
Bframe.pack(side="bottom")
#Iframe.pack(side="top")
x.mainloop()	