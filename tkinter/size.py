import tkinter as tk

root = tk.Tk()

# set size of root window

# root.minsize(300,300)           # mininum size
# root.maxsize(1200,800)          # maximum size

root.geometry('800x600+275+50')         # cab be resized to max or min
# root.resizable(0,0)               # can't be resized

# Title
root.title('Size')

root.mainloop()
