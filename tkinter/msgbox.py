from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("350x200+200+100")


btn1 = Button(root, text='Click', font=("", 12),
              command=lambda: messagebox.showinfo("Info", "Welcome"))
btn1.pack()


# messagebox.showinfo("Welcome", "Welcome Ankit,\nGreat job! ")
x = messagebox.askyesno("Start study", "Start study?")
# print(x)
if x == False:
    root.destroy()

root.mainloop()
