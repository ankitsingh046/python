import tkinter as tk
root = tk.Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Link Windows')
root.iconbitmap('icon.ico')


def login():
    f2 = tk.Frame(root, background="black")
    f2.place(x=0, y=0, height=400, width=400)

    l1 = tk.Label(f2, text='Login Page', font=('Arial', 20), fg='red', bg='black')
    l1.place(x=130, y=20)

    l1 = tk.Label(f2, text='Enter Name:', font=('Arial', 12), fg='white', bg='black')
    l1.place(x=50, y=100)
    e1 = tk.Entry(f2, font=('Arial', 12))
    e1.place(x=200, y=100, width=120)

    l2 = tk.Label(f2, text='Enter Password:', font=('Arial', 12), fg='white', bg='black')
    l2.place(x=50, y=150)
    e2 = tk.Entry(f2, font=('Arial', 12), show="*")
    e2.place(x=200, y=150, width=120)

    # e2 = tk.Entry(f2, font=('Arial', 14))
    # e2.pack()
    b2 = tk.Button(f2, text="Login", font=("", 12), command=home)
    b2.place(x=130, y=200, height=25, width=100)
    b3 = tk.Button(f2, text="<--", font=("", 10), command=home)
    b3.place(x=0, y=0, height=20)


def register():

    f3 = tk.Frame(root, background="black")
    f3.place(x=0, y=0, height=400, width=400)

    l1 = tk.Label(f3, text='Registration Page', font=('Arial', 20), fg='red', bg='black')
    l1.place(x=90, y=20)

    l1 = tk.Label(f3, text='Enter Name:', font=('Arial', 12), fg='white', bg='black')
    l1.place(x=50, y=100)
    e1 = tk.Entry(f3, font=('Arial', 12))
    e1.place(x=200, y=100, width=120)

    l3 = tk.Label(f3, text='Enter Email:', font=('Arial', 12), fg='white', bg='black')
    l3.place(x=50, y=150)
    e3 = tk.Entry(f3, font=('Arial', 12))
    e3.place(x=200, y=150, width=120)

    l2 = tk.Label(f3, text='Enter Password:', font=('Arial', 12), fg='white', bg='black')
    l2.place(x=50, y=200)
    e2 = tk.Entry(f3, font=('Arial', 12))
    e2.place(x=200, y=200, width=120)

    # e2 = tk.Entry(f2, font=('Arial', 14))
    # e2.pack()
    b2 = tk.Button(f3, text="Register", font=("", 12), command=home)
    b2.place(x=130, y=250, height=25, width=100)
    b3 = tk.Button(f3, text="<--", font=("", 10), command=home)
    b3.place(x=0, y=0, height=20)


def home():
    f1 = tk.Frame(root, background="#005eff")
    f1.place(x=0, y=0, height=400, width=400)
    b1 = tk.Button(f1, text='Login', font=("", 16), command=login)
    b1.place(x=100, y=50)
    b2 = tk.Button(f1, text='Register', font=("", 16), command=register)
    b2.place(x=200, y=50)


home()
root.mainloop()
