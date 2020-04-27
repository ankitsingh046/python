import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('425x350')
root.resizable(0, 0)
root.title('Notebook')

top_frame = tk.Frame(root, background='Grey')
top_frame.place(x=0, y=0, width=425, height=20)


def login():
    pass


button = tk.Button(top_frame, text='Login', command=login)
button.pack(side=tk.LEFT)

tab_menu = tk.Frame(root)
tab_menu.place(x=0, y=25, width=425, height=330)

note_b = ttk.Notebook(tab_menu)
note_b.place(x=0, y=0, height=325, width=425)

tab_f1 = tk.Frame(note_b, background="cyan")
note_b.add(tab_f1, text='Tab1')


tab_f2 = tk.Frame(note_b, bg="Gray")
note_b.add(tab_f2, text='Tab2')

btn1 = tk.Button(tab_f1, text="sign")
btn1.pack()

entry = tk.Entry(tab_f2, font=('Arial', 20))
entry.pack()


root.mainloop()
