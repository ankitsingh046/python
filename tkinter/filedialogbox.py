from tkinter import *
from tkinter import filedialog
import os
root = Tk()
root.minsize(200, 150)


def open_file():

    s = filedialog.askopenfile(initialdir="/", title='Select File',
                               filetypes=(('text files', '.txt'), ('all files', '*.*')))
    text.delete(1.0, END)
    for i in s:
        text.insert(INSERT, i)


button = Button(root, text='open', width=15, command=open_file).pack(side=TOP, pady=5)

text = Text(root)
text.pack(fill=BOTH, padx=5, pady=5, expand=True)


root.mainloop()
