from tkinter import *

root = Tk()
root.minsize(300, 250)
root.title('Root')


def open_win():
    top = Toplevel()
    top.minsize(300, 250)
    top.title("top win")
    btn2 = Button(top, text='close', command=top.destroy)
    btn2.pack()


btn1 = Button(root, text='open', command=open_win)
btn1.pack()

root.mainloop()
