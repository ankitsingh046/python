import tkinter as tk
# from tkinter import messagebox

root = tk.Tk()
root.geometry('400x300')

c = 1


def show(v):
    global c
    if v['text'] == "":
        c += 1
        if c % 2 == 0:
            v['text'] = '0'
        else:
            v['text'] = 'X'

    if ((b1['text'] == '0' and b2['text'] == '0' and b3['text'] == '0') or
        (b4['text'] == '0' and b5['text'] == '0' and b6['text'] == '0') or
        (b7['text'] == '0' and b8['text'] == '0' and b9['text'] == '0') or
        (b1['text'] == '0' and b4['text'] == '0' and b7['text'] == '0')or
        (b2['text'] == '0' and b5['text'] == '0' and b8['text'] == '0')or
        (b3['text'] == '0' and b6['text'] == '0' and b9['text'] == '0')or
        (b1['text'] == '0' and b5['text'] == '0' and b9['text'] == '0')or
            (b3['text'] == '0' and b5['text'] == '0' and b7['text'] == '0')):
        print('palyer1 wins')

    else:
        if ((b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X') or
            (b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X') or
            (b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X') or
            (b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X') or
            (b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X') or
            (b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X') or
            (b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X') or
                (b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X')):
            print('palyer2 wins')


b1 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b1))
b2 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b2))
b3 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b3))
b4 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b4))
b5 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b5))
b6 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b6))
b7 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b7))
b8 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b8))
b9 = tk.Button(root, text="", width=15, height=5, command=lambda: show(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
root.mainloop()
()
