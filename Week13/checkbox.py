from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=E)
blackbutton = Button(master, text ='Black', fg ='black', command=lambda:print(var1.get(), var2.get()))
blackbutton.grid( row=4, sticky=E)
master.mainloop()