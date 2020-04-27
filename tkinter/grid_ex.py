import tkinter as tk

root = tk.Tk()

# set size of root window
root.geometry('350x250')     # cab be resized to max or min

# Grid Example
# function


def show():
    name = name_entry.get()   # get entry value
    passw = pass_entry.get()  # get entry value
    print(f'{name}, {passw}')


# labels
name_label = tk.Label(root,
                      text='Enter name: ',
                      font=('Arial', 12)
                      )

pass_label = tk.Label(root,
                      text='Enter Password: ',
                      font=('arial', 12)
                      )

# Entry
name_entry = tk.Entry(root,
                      font=('Arial', 12),
                      )

pass_entry = tk.Entry(root,
                      font=('Arial', 12),
                      show="*"   # show '*' instead of characters
                      )
# button
submit_btn = tk.Button(root,
                       text='Submit',
                       font=('Arial', 12),
                       width='12',
                       bg='Grey',
                       fg='White',
                       #    command=show
                       )

submit_btn.config(command=show)
# submit_btn.bind("<Button>",show)

# grid
name_label.grid(row=0, column=0, pady=25, sticky=tk.W)
name_entry.grid(row=0, column=1, pady=25)
pass_entry.grid(row=1, column=1, pady=25)
pass_label.grid(row=1, column=0, pady=25)
submit_btn.grid(row=2, columnspan=2, pady=25)


root.mainloop()
