import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('300x200')


def show(e=""):
    messagebox.showinfo('Welcome', 'Welcome')


root.bind("<Return>", show)

b1 = tk.Button(root, text='click', command=show)
b1.pack()

root.mainloop()
