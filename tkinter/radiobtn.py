from tkinter import *

root = Tk()
root.geometry('400x400')

# variables
entry_var = StringVar()
name_var = IntVar()


# function
def show():
    if name_var.get() == 1:
        entry_var.set("Male")
    if name_var.get() == 2:
        entry_var.set("Female")


# Radio button
male_radio = Radiobutton(root, text='Male', value=1, variable=name_var, command=show)
male_radio.pack()

female_radio = Radiobutton(root, text='Female', value=2, variable=name_var, command=show)
female_radio.pack()

# Entry
entry1 = Entry(root, textvariable=entry_var)
entry1.pack()

root.mainloop()
