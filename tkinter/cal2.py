import tkinter as tk
root = tk.Tk()
root.geometry('425x280')
# root.resizable(0, 0)
root.title('Calc')
root.iconbitmap('icon.ico')
root.configure(background='Black')

# Entry
a = tk.StringVar()
entry = tk.Entry(root, font=('Arial', 30), justify="right",
                 textvariable=a
                 )
# entry.pack(side=tk.TOP, fill=tk.X)
entry.grid(row=0, columnspan=4)


def show(c):
    a.set(a.get()+c)


def result():
    ex = a.get()
    a.set(eval(ex))


def clear():
    # entry.delete(0, tk.END)
    a.set('')


# b = [tk.Button()]*16
b = [""]*16
data = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "C", "0", "=", "/"]
x = 1
y = 0
k = 0
for i in range(4):
    for j in range(4):
        b[k] = tk.Button(text=data[k], font=("", 25))
        b[k].grid(row=x, column=j, sticky=tk.W)
        k += 1
        # y += 1
    x += 1
    y = 0


root.mainloop()
