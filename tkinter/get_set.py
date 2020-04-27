import tkinter as tk

root = tk.Tk()

# set size of root window
root.geometry('350x250')     # cab be resized to max or min
root.minsize(320, 220)
# Grid Example
# function


def set_pass_from_name():
    name = name_var.get()       # get entry value
    # passw = output_var.get()      # get entry value
    # print(f'{name}, {passw}')
    name_var.set("")
    output_var.set(name)


# labels
name_label = tk.Label(root,
                      text='Enter name: ',
                      font=('Arial', 12)
                      )

output_label = tk.Label(root,
                        text='output: ',
                        font=('arial', 12)
                        )

# variables
name_var = tk.StringVar()
output_var = tk.StringVar()


# Entry

name_entry = tk.Entry(root,
                      font=('Arial', 12),
                      textvariable=name_var
                      )

output_entry = tk.Entry(root,
                        font=('Arial', 12),
                        #   show="*",   # show '*' instead of characters,
                        textvariable=output_var,  # pass value to variable
                        state='readonly'
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

submit_btn.config(command=set_pass_from_name)
# submit_btn.bind("<Button>",show)

# grid
name_label.grid(row=0, column=0, pady=25, sticky=tk.W)
name_entry.grid(row=0, column=1, pady=25)
output_entry.grid(row=2, column=1, pady=25)
output_label.grid(row=2, column=0, pady=25)
submit_btn.grid(row=1, columnspan=2, pady=25)


root.mainloop()
