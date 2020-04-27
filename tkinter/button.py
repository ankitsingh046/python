import tkinter as tk


root = tk.Tk()

# set size of root window
root.geometry('300x200')         # cab be resized to max or min

# function


def show():
    root.configure(background="Pink")


# Button Widget
button_ex = tk.Button(root,
                      text='Submit',
                      font=('Arial', 12),
                      width='20',
                      fg='Red',
                      bg="#d5f7f4",
                      # command=show  # on click calls function
                      )

# config used to set functionality externally
button_ex.config(command=show)


button_ex.pack()

root.mainloop()
