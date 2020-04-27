import tkinter as tk
# from tkinter import messagebox

root = tk.Tk()
root.geometry('300x200')


def show(c):
    # b1.configure(text='abkit')
    c['text'] = 'Ankit'
    c['bg'] = "grey"
    c['fg'] = 'white'
    c['width'] = 10
    c['height'] = 5
    c['font'] = ('Arial', 20)


b1 = tk.Button(root, text='click', command=lambda: show(b1))
b1.pack()

root.mainloop()
