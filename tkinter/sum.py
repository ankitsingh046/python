import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
# title
root.title("Sum")
# size of window
root.geometry('400x300')

# label
num1_label = tk.Label(root, text='Enter First Number:', font=('Arial', 12))
num1_label.grid(row=0, column=0, sticky=tk.W)

num2_label = tk.Label(root, text='Enter Second Number:', font=('Arial', 12))
num2_label.grid(row=1, column=0, sticky=tk.W)

# Entry
# num1_var = tk.StringVar()
num1_entry = tk.Entry(root, font=('Arial', 12),
                      # textvariable=num1_var
                      )
num1_entry.grid(row=0, column=1)

# num2_var = tk.StringVar()
num2_entry = tk.Entry(root, font=('Arial', 12),
                      # textvariable=num2_var
                      )
num2_entry.grid(row=1, column=1)


result_var = tk.DoubleVar()
result_entry = tk.Entry(root, font=('Arial', 12), textvariable=result_var,
                        state='readonly'
                        )
result_entry.grid(row=4, columnspan=2)


# function
def add(e):
    if num1_entry.get() == '' or num2_entry.get() == '':
        messagebox.showerror('Error!', 'Empty fields')
    else:
        try:
            num1 = float(num1_entry.get())
            num2 = float(num2_entry.get())

        except:
            messagebox.showerror('Error', 'input digits only')
        else:
            if (e == 1):
                result = num1+num2
                result_var.set(result)

            if e == 2:
                result = num1-num2
                result_var.set(result)

            # num1_var.set("")
            # num2_var.set("")


# button
btn = tk.Button(root, text="Add", font=('Arial', 12),
                command=lambda: add(1)
                )

btn.grid(row=2, columnspan=2, pady=25)

btn_sub = tk.Button(root, text="Subtract", font=('Arial', 12),
                    command=lambda: add(2)
                    )

btn_sub.grid(row=3, columnspan=2, pady=25)
result_var.set('')

root.mainloop()
