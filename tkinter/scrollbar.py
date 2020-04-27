from tkinter import *
root = Tk()
root.geometry('350x250')
root.title('ScrollBar')

frame1 = Frame(root)

scroll = Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame1, yscrollcommand=scroll.set)
for i in range(1, 100):
    listbox.insert(END, i)
listbox.pack(side=LEFT, fill=Y)

scroll.config(command=listbox.yview)

frame1.pack()

root.mainloop()
