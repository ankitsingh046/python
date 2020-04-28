from tkinter import *
from tkinter import simpledialog


root = Tk()


def pop():
    s = simpledialog.askstring("Input string", 'Please enter your name')
    print(s)


btn1 = Button(root, text='popup', command=pop)
btn1.pack()

root.mainloop()
