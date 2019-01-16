
from tkinter import * 
from tkinter.filedialog import *
from app import *
from PIL import Image,ImageTk
import os
x=None
newpath = r'C:/__editedpics__'
if not os.path.exists(newpath):
	os.makedirs(newpath)
location="C:/__editedpics__"
open_file=None
save_file=None
img1=None
img2=None
root = Tk()
history=[]
address=[]
# f1 = Frame(root,bd=2, width = 500, height =500)
# f1.pack(side=LEFT, expand = 1)

def main_image():
	#print(type(path))
	#print(type(canvas))
	canvas.delete("all")
	canvas.create_image(150,150, image=img1)

def preview_image():

	      
	canvas1.delete("all")
	canvas1.create_image(150,150, image=img2)

##########################opening and saving a file########################
def open_image(): 
	global open_file
	open_file= askopenfilename() 
	print(open_file)
	global img1
	address.append(open_file)
	image = Image.open(open_file)
	img1 =ImageTk.PhotoImage(image)
	address.append(open_file)
	history.append(img1)
	print(len(history))
	main_image()


def close_image():
	global save_file
	save_file= askdirectory()
	k=open_file.split("/")
	p=k[-1]
	os.rename(open_file,save_file+"/"+"p.jpg")



f3 = Frame(root, bg = "black",bd=2, width = 10, height =7)
f3.pack(side=TOP)
Select = Button(f3, text="Select a Image", fg="brown",command=open_image,width=80)
Select.pack()

f3 = Frame(root, bg = "black",bd=2, width = 10, height =7)
f3.pack(side=BOTTOM)
close = Button(f3, text="Save", fg="brown",width=80,command=close_image)
close.pack()
#######################opening and saving a file#####################


###################### rotating an image########################3


f = Frame(root ,bd=5,width = 1, height =1080)
f.pack(side=LEFT)

def pix():
	s=pixels.get()
	print(s)
#rotating the image
def call_rotate():
	path=address[-1]
	global img1
	p=rotate(path)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)
	


Rotate = Button(f, text="Rotate", fg="brown",command=call_rotate)
Rotate.grid(column=2,row=0,padx=10, pady=50)
###################### rotating an image########################3

#bluring the image
def call_blur():
	path=address[-1]
	global img1
	p=blur1(path)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

blur = Button(f, text="Blur", fg="brown",command=call_blur)
blur.grid(column=2,row=5,padx=10, pady=50)

#change to black and white
def call_b2w():
	path=address[-1]
	global img1
	p=bw(path)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

b2w = Button(f, text=" B&W ", fg="brown",command=call_b2w)
b2w.grid(column=2,row=10,padx=10, pady=50)

#corp the image
def accept():
	
	length=int(pixels.get())
	width=int(pixel.get())
	path=address[-1]
	global img1
	p=crop1(path,length,width)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

pixels=Entry(f, width = 10)
pixels.grid(column=0,row=20)	

Label(f, text = "x").grid(column = 1, row = 20) 
pixel=Entry(f, width = 10)
pixel.grid(column=2,row=20)


crop = Button(f, text="Crop", fg="brown",command=accept)
crop.grid(column=3,row=20, pady=10)


############ original image of selected by the user#############
f1 = Frame(root,bd=2, width = 500, height =500)
f1.pack(side=LEFT, expand = 1)
Label(f1, text = "YOUR image").pack()
Label(f1).pack()

canvas = Canvas(f1, width = 300, height = 300)

canvas.pack()

##############preview of the image and the filter####################
f11 = Frame(root,bd=2, width = 500, height =500)
f11.pack(side=LEFT,expand=1)
Label(f11, text = "preview").pack()
Label(f11).pack()
canvas1 = Canvas(f11, width = 300, height = 300)      
canvas1.pack()






###############the filter side part(right sided part)  ###############
f2 = Frame(root,bd=2, width = 500, height =500)
f2.pack(side=RIGHT)
###########the filter button#########


cool = Button(f2, text="Cool", fg="brown")
cool.grid(column=3,row=0,padx=10, pady=30)
pop = Button(f2, text="PoP", fg="brown")
pop.grid(column=3,row=5,padx=10, pady=30)
chrome = Button(f2, text="Chrome", fg="brown")
chrome.grid(column=3,row=10,padx=10, pady=30)
film = Button(f2, text="Film", fg="brown")
film.grid(column=3,row=20, pady=10,padx=30)

############the brightness and contrast sharpness and the color##########

###############contrast slider
def apply_contrast(value):
	path=address[-1]
	global img1
	p=contrast1(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)


def sel_contrast():
	v=int(var.get())
	if v == 0:
		pass
	else:
		apply_contrast(int(var.get()))

def preview_contrast(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		p=contrast1(path,val)
		img2=p.pop()
		preview_image()
   
	
var = DoubleVar()
Label(f2, text = "Contrast").grid(column=2,row=29)
scale1 = Scale( f2 , from_=-10.0, to=10.0,variable = var,command=preview_contrast)
scale1.grid(column=2, row=30)
set_bright = Button(f2, text="Apply", command=sel_contrast)
set_bright.grid(column=2,row=31)
####################brightness slider


def apply_brightness(value):
	path=address[-1]
	global img1
	p=brightness1(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)


def sel_brightness():
	v=int(var.get())
	if v == 0:
		pass
	else:
		apply_brightness(int(var.get()))

def preview_brightness(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		p=brightness1(path,val)
		img2=p.pop()
		preview_image()

Label(f2, text = "Brightness").grid(column=4,row=29)
var1= DoubleVar()
scale2 = Scale( f2, from_=-10.0, to=10.0,variable = var1,command=preview_brightness)
scale2.grid(column=4, row=30)
set_bright = Button(f2, text="Apply", command=sel_brightness)
set_bright.grid(column=4,row=31)
#########################################sharpness slider

def apply_sharpness(value):
	print("apply_sharpness")
	path=address[-1]
	global img1
	p=sharpness1(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)


def sel_sharpness():
	v=int(var3.get())
	
	if v == 0:
		pass
		

	else:

		apply_sharpness(int(var3.get()))
		

def preview_sharpness(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		p=sharpness1(path,val)
		img2=p.pop()
		preview_image()


Label(f2, text = "Sharpness",pady=5).grid(column=2,row=59)
var3= DoubleVar()
scale3 = Scale( f2, from_=-10.0, to=10.0,variable = var3,command=preview_sharpness )
scale3.grid(column=2, row=60)
set_bright = Button(f2, text="Apply", command=sel_sharpness)
set_bright.grid(column=2,row=61)


##########################hue slider

def apply_hue(value):
	print("apply_hue")
	path=address[-1]
	global img1
	p=hue1(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)


def sel_hue():
	v=float(var4.get())

	apply_hue(v)
		

def preview_hue(val):
	v=int(val)
	path=address[-1]

	global img2
	p=hue1(path,v)
	img2=p.pop()
	preview_image()


Label(f2, text = " Color " ,pady=5).grid(column=4,row=59)
var4= DoubleVar()
scale3 = Scale( f2, from_=0, to=10,variable = var4,command=preview_hue)
scale3.grid(column=4, row=60)
set_bright = Button(f2, text="Apply", command=sel_hue)
set_bright.grid(column=4,row=61)



###############undo button


def undo_button():
	if len(history)== 0  :
		pass
		print(len(history))
	

	else:
		print(len(history))
		global img1
		img1=history.pop()
		address.pop()
		main_image()



undo = Button(f2, text="Undo", fg="brown",bg="blue",command=undo_button)
undo.grid(column=3,row=90, pady=50,padx=30)



root.mainloop()