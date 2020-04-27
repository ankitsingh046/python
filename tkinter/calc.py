import tkinter as tk
root = tk.Tk()
root.geometry('500x400')
root.resizable(0, 0)
root.title('Calc')
root.iconbitmap('icon.ico')
root.configure(background='Black')

# Entry
a = tk.StringVar()
entry = tk.Entry(root, font=('Arial', 30), justify="right",
                 textvariable=a
                 )
entry.pack(side=tk.TOP, fill=tk.X)
# entry.place(x=0, y=0, width=425, height=50)


def show(c):
    a.set(a.get()+c)


def result():
    ex = a.get()
    try:
        a.set(eval(ex))
    except:
        a.set('Err')


def clear():
    # entry.delete(0, tk.END)
    a.set('')


# b = [tk.Button()]*16
b = [""]*16
data = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "C", "0", ".", "/"]
x = 5
y = 55
k = 0
for i in range(4):
    for j in range(4):
        b[k] = tk.Button(text=data[k], font=("", 25), activebackground='yellow')

        b[k].place(x=x, y=y, width=100, height=50)
        k += 1
        x += 105
    x = 5
    y += 55
e = tk.Button(text="=", font=("", 25), activebackground='yellow')
e.place(x=5, y=275, width=415, height=50)

b[0].configure(command=lambda: show(data[0]))
b[1].configure(command=lambda: show(data[1]))
b[2].configure(command=lambda: show(data[2]))
b[3].configure(command=lambda: show(data[3]))
b[4].configure(command=lambda: show(data[4]))
b[5].configure(command=lambda: show(data[5]))
b[6].configure(command=lambda: show(data[6]))
b[7].configure(command=lambda: show(data[7]))
b[8].configure(command=lambda: show(data[8]))
b[9].configure(command=lambda: show(data[9]))
b[10].configure(command=lambda: show(data[10]))
b[11].configure(command=lambda: show(data[11]))
b[12].configure(command=clear)
b[13].configure(command=lambda: show(data[13]))
b[14].configure(command=lambda: show(data[14]))
b[15].configure(command=lambda: show(data[15]))
e.configure(command=result)

root.mainloop()
