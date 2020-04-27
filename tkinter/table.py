import tkinter as tk
# from tkinter import messagebox

root = tk.Tk()
# title
root.title("Table")
# size of window
root.geometry('400x300')


entry_var = tk.IntVar()
entry = tk.Entry(root, font=('Arial', 12), textvariable=entry_var)
entry.pack()


def calc():
    val = entry_var.get()
    for i in range(1, 11):
        print(val*i)
    entry.delete(0, tk.END)


btn = tk.Button(root, text='Click', command=calc)
btn.pack()

entry.delete(0, tk.END)
root.mainloop()
