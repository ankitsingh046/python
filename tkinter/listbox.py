from tkinter import *
root = Tk()
root.geometry('350x250')

list1 = Listbox(root, selectmode=SINGLE)  # MULTIPLE, #EXTENDED
list1.insert(1, 'C++')
list1.insert(2, 'java')
list1.insert(3, 'Python')

list1.pack()


def print_me():
    clicked_items = list1.curselection()
    # print(clicked_items)
    for item in clicked_items:
        print(list1.get(item))


def del_me():
    clicked_items = list1.curselection()
    # print(clicked_items)
    for item in clicked_items:
        list1.delete(item)


btn1 = Button(root, text='print', command=print_me).pack()
btn_del = Button(root, text='del', command=del_me).pack()
root.mainloop()
