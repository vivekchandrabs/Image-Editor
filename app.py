import os
from PIL import Image,ImageTk
from PIL import ImageFilter,ImageEnhance
import colorsys

def rotate(i):
	p=[]#first the pil image will be appended and then the tkinter image will be appended
	im=Image.open(i)
	out=im.transpose(Image.ROTATE_90)
	image_tk = ImageTk.PhotoImage(out)
	p.append(out)
	p.append(image_tk)
	print(type(image_tk))
	return p
def bw(i):
	p=[]
	im=Image.open(i)
	bw1=im.convert('L')
	image_tk = ImageTk.PhotoImage(bw1)
	p.append(bw1)
	p.append(image_tk)
	print(type(image_tk))
	return p
def crop1(i,length,width):
	p=[]
	size=(length,width)
	im =Image.open(i)
	im.thumbnail(size)
	image_tk = ImageTk.PhotoImage(im)
	p.append(im)
	p.append(image_tk)
	print(type(image_tk))
	return p


	
def blur1(i):
	p=[]
	im=Image.open(i)
	blurred = im.filter(ImageFilter.BLUR)
	blurred = blurred.filter(ImageFilter.BLUR)
	image_tk = ImageTk.PhotoImage(blurred)
	p.append(blurred)
	p.append(image_tk)
	return p


def contrast1(i,factor):
	factor=int(factor)
	p=[]
	im=Image.open(i)
	c = ImageEnhance.Contrast(im)
	c = c.enhance(factor)
	image_tk = ImageTk.PhotoImage(c)
	p.append(c)
	p.append(image_tk)
	return p



def brightness1(i,factor):
	v=int(factor)
	p=[]
	img=Image.open(i)
	enhancer=ImageEnhance.Brightness(img)
	c=enhancer.enhance(v)
	image_tk = ImageTk.PhotoImage(c)
	p.append(c)
	p.append(image_tk)
	return p


def sharpness1(i,factor):
	v=int(factor)
	p=[]
	img=Image.open(i)
	enhancer=ImageEnhance.Sharpness(img)
	c=enhancer.enhance(v)
	image_tk = ImageTk.PhotoImage(c)
	p.append(c)
	p.append(image_tk)
	return p

def hue1(i,v):
	
	
	p=[]
	img = Image.open(i)    
	r,g,b = img.split()
	Hdat = []
	Ldat = []
	Sdat = []    
	for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()):
		h,l,s = colorsys.rgb_to_hls(rd/v,gn/v,bl/v)
		Hdat.append(int(h*v))
		Ldat.append(int(l*v))
		Sdat.append(int(s*v))

	r.putdata(Hdat)
	g.putdata(Ldat)
	b.putdata(Sdat)
	newimg = Image.merge('RGB',(r,g,b))
	image_tk = ImageTk.PhotoImage(newimg)
	p.append(newimg)
	p.append(image_tk)
	return p