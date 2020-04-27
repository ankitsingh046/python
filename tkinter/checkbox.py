from tkinter import *

root = Tk()
root.geometry('400x400')
entry_var = StringVar()
mail_var = IntVar()
name_var = IntVar()


def show():
    s = ""
    if name_var.get() == 1:
        s += "name"
    if mail_var.get() == 1:
        s += " Email"
    entry_var.set(s)


ch1 = Checkbutton(root, text='name', variable=name_var, command=show)
ch1.pack()


ch2 = Checkbutton(root, text='Email', variable=mail_var)
ch2.pack()


btn1 = Button(root, text='show', command=show)
btn1.pack()


entry1 = Entry(root, textvariable=entry_var)
entry1.pack()
root.mainloop()
