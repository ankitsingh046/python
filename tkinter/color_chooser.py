from tkinter import *
from tkinter import colorchooser


root = Tk()
root.minsize(300, 200)


def show_color():
    color = colorchooser.askcolor(title='Choose color')
    root.configure(background=color[1])
    # print(color[1])


btn1 = Button(root, text='color', command=show_color)
btn1.pack()

root.mainloop()
