from tkinter import *
root = Tk()
root.geometry('350x300')


def show():
    txt.search(1.0, END)


txt = Text(root, height=15, width=25, ).pack()
# txt.insert(INSERT, 'Hi')


btn = Button(root, text='Submit', command=show).pack()
root.mainloop()
