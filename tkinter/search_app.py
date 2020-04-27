from tkinter import *
import wikipedia


root = Tk()
root.minsize(450, 350)
root.title('Search App')


def show():
    entry_val = entry.get()
    try:
        answer.delete(1.0, END)
        answer_val = wikipedia.summary(entry_val)
    except:
        answer.insert(INSERT, "Something went Wrong")
    else:
        answer.insert(INSERT, answer_val)


def show1(e):
    entry_val = entry.get()
    answer.delete(1.0, END)
    try:

        answer_val = wikipedia.summary(entry_val)
    except:
        answer.insert(INSERT, "Something went Wrong")
    else:
        answer.insert(INSERT, answer_val)


# Top Frame
top_frame = Frame(root, background="#cfcdc8")
# Entry Box
entry = Entry(top_frame, width=40, font=("", 12))
entry.bind('<Return>', show1)
entry.focus()
entry.pack(ipady=5, pady=5)
# search Button
btn1 = Button(top_frame, text="Search",  width=10, command=show)

btn1.pack(pady=5)
top_frame.pack(side=TOP, fill=X)

# Bottom frame
bottom_frame = Frame(root, background="#cfcdc8")

# scrollbar
scroll = Scrollbar(bottom_frame)
scroll.pack(side=RIGHT, fill=Y)

# text
answer = Text(bottom_frame, font=("Arial", 12), wrap=WORD, yscrollcommand=scroll.set)
answer.pack(fill=BOTH, padx=5, pady=5, expand=True)

scroll.config(command=answer.yview)

bottom_frame.pack(fill=BOTH, expand=TRUE)


root.mainloop()
