import tkinter as tk

root = tk.Tk()

root.geometry('300x250')

a = tk.StringVar()


def set():
    root.configure(background=a.get())


s1 = tk.Spinbox(root, font=('Arial', 12),
                values=['red', 'green', 'blue', 'yellow', 'black'],
                textvariable=a
                )
s1.pack()

btn1 = tk.Button(root, text='Set', font=('Arial', 12), command=sext)
btn1.pack()
root.mainloop()
