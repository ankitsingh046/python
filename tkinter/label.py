import tkinter as tk

root = tk.Tk()

# set size of root window

# root.minsize(300,300)           # mininum size
# root.maxsize(1200,800)          # maximum size

root.geometry('600x300')         # cab be resized to max or min
# root.resizable(0,0)               # can't be resized

# Label Widget

label_ex = tk.Label(root,
                    text="Welcome",
                    font=('Arial', 12),
                    bg='#f5970a',
                    fg='white',
                    width='18',
                    height='1'
                    )

label_ex.pack(fill=tk.X)

root.mainloop()
