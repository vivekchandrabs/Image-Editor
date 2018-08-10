# from tkinter import *      
# root = Tk()      
# canvas = Canvas(root, width = 300, height = 300)      
# canvas.pack()      
# img = PhotoImage(file="A8R.gif")      
# canvas.create_image(150,150, image=img)      
# mainloop()   

#to display the image.in the canvas.

# from tkinter import *

# root = Tk()
# frame = Frame(root)
# frame.grid()

# bottomframe = Frame(root)
# # bottomframe.pack( side = BOTTOM )

# # redbutton = Button(frame, text="Red", fg="red")
# # redbutton.pack( side = LEFT)

# # greenbutton = Button(frame, text="Brown", fg="brown")
# # greenbutton.pack( side = LEFT )

# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.grid( column=0,row=1000)

# # blackbutton = Button(bottomframe, text="Black", fg="black")
# # blackbutton.pack( side = BOTTOM)

# root.mainloop()




from tkinter import * 
from tkinter import filedialog
x=None
root = Tk()


f3 = Frame(root, bg = "black",bd=2, width = 10, height =7)
f3.pack(side=TOP)
B1 = Button(f3, text="Brown", fg="brown",width=80)
B1.pack()

f3 = Frame(root, bg = "black",bd=2, width = 10, height =7)
f3.pack(side=BOTTOM)
B1 = Button(f3, text="Brown", fg="brown",width=80)
B1.pack()

f = Frame(root ,bd=5, bg="BLACK",width = 1, height =1080)
f.pack(side=LEFT)

def pix():
	s=pixels.get()
	print(s)

B1 = Button(f, text="Brown", fg="brown")
B1.grid(column=2,row=0,padx=10, pady=100)
B1 = Button(f, text="Brown", fg="brown")
B1.grid(column=2,row=5,padx=10, pady=100)
B1 = Button(f, text="Brown", fg="brown")
B1.grid(column=2,row=10,padx=10, pady=10)
B1 = Button(f, text="Brown", fg="brown")


B1.grid(column=3,row=20, pady=10)
pixels=Entry(f, width = 10)
pixels.focus_set()
s=pixels.get()
print(s)
pixels.grid(column=0,row=20)	
Label(f, text = "x").grid(column = 1, row = 20) 
pixel=Entry(f, width = 10, textvariable = x)
pixel.grid(column=2,row=20)


f1 = Frame(root, bg = "BLACK",bd=2, width = 500, height =500)
f1.pack(side=LEFT, expand = 1)

Label(f1, text = "YOUR image").pack()
Label(f1).pack()
canvas = Canvas(f1, width = 300, height = 300)      
canvas.pack()
img1 = PhotoImage(file="A8R.gif")      
canvas.create_image(150,150, image=img1)



f11 = Frame(root, bg = "GREEN",bd=2, width = 500, height =500)
f11.pack(side=LEFT,expand=1)
Label(f11, text = "preview").pack()
Label(f11).pack()
canvas1 = Canvas(f11, width = 300, height = 300)      
canvas1.pack()    
img = PhotoImage(file="A8R.gif")      
canvas1.create_image(150,150, image=img)

f2 = Frame(root, bg = "black",bd=2, width = 500, height =500)
f2.pack(side=RIGHT)

B1 = Button(f2, text="Brown", fg="brown")
B1.grid(column=2,row=0,padx=10, pady=100)
B1 = Button(f2, text="Brown", fg="brown")
B1.grid(column=2,row=5,padx=10, pady=100)
B1 = Button(f2, text="Brown", fg="brown")
B1.grid(column=2,row=10,padx=10, pady=10)
B1 = Button(f2, text="Brown", fg="brown")
B1.grid(column=3,row=20, pady=10,padx=40)







# f3 = Frame(f, bg = "red", width = 500)
# f3.pack(side=LEFT, expand = 1, pady = 50, padx = 50)

# f2 = Frame(root, bg = "black", height=100, width = 100)
# f2.pack(side=LEFT, fill = Y)

# b = Button(f2, text = "test")
# b.pack()

# b = Button(f3, text = "1", bg = "red")
# b.grid(row=1, column=3)
# b2 = Button(f3, text = "2")
# b2.grid(row=1, column=4)
# b3 = Button(f3, text = "2")
# b3.grid(row=2, column=0)

root.mainloop()