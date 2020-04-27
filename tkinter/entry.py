import tkinter as tk

root = tk.Tk()

# set size of root window
root.geometry('400x200')         # cab be resized to max or min

# text /= ""


def show(e):
    global text
    text = entry_ex.get()
    msg = tk.Message(root, text=text)
    msg.pack(side=tk.BOTTOM)


# Entry Widget
entry_ex = tk.Entry(root,
                    font=('Arial', 12),
                    width='20',
                    fg='Red',
                    bg="#d5f7f4"

                    # show="*"
                    )

entry_ex.bind('<KeyRelease>', show)

entry_ex.pack()

# result_label=LAb

root.mainloop()
