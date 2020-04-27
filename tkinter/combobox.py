from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('300x250')


val = ['C++', 'Java', 'Python', 'Php']
val2 = list(range(1, 21))

combo1 = ttk.Combobox(root, values=val2, height=5)  # opt: height, width,
# combo1.current(0)
combo1.set("Select")
combo1.pack()


def show():
    if combo1.get() == 'Select':
        print('No value selected')
    else:
        print(combo1.get())


btn = Button(root, text='Show', command=show).pack()

root.mainloop()
