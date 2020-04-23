import tkinter as tk

root = tk.Tk()

# set size of root window
root.geometry('300x200')         # cab be resized to max or min

# title
root.title("Event Binding")

# function
x=1
def show(e):
    global x
    x+=1
    if x%2==0:
        root.configure(background="Grey")
    else:
        root.configure(background="yellow")


# def show1(e):
#     root.configure(background="Pink")


# def show2(e):
#     root.configure(background="Green")


# Button Widget
button_ex = tk.Button(root,
                      text='Submit',
                      font=('Arial', 12),
                      width='20',
                      fg='Red',
                      bg="#d5f7f4",
                      # command=show  # on click calls function
                      )

# button_ex.config(command=show)        # config used to set functionality externally

# bind the function on event single  click
button_ex.bind('<Button-1>', lambda e: root.configure(background="red"))
button_ex.bind('<Button-2>',  lambda e: root.configure(background="Green"))
button_ex.bind('<Button-3>', lambda e: root.configure(background="Blue"))

# bind the function on event double  click
button_ex.bind('<Double-1>', lambda e: root.configure(background="black"))
button_ex.bind('<Double-2>', lambda e: root.configure(background="yellow"))
button_ex.bind('<Double-3>', lambda e: root.configure(background="cyan"))

# bind function on mouse enter and leave 
button_ex.bind('<Enter>', lambda e:root.configure(background='coral'))
button_ex.bind('<Leave>', lambda e : root.configure(background='cyan'))

# Motion event binding
button_ex.bind('<Motion>', show)

button_ex.pack()

# change root window color on keypress event
root.bind('<Key-a>', lambda e:root.configure(background='orange'))

root.bind('1', lambda e:root.configure(background='yellow'))

root.bind('<Shift-Up>', lambda e:root.configure(background='grey'))

root.bind('<Alt-Down>', lambda e:root.configure(background='White'))

root.bind('<Control-Right>', lambda e:root.configure(background='yellow'))

# change root window color on mouse enter and leave event
root.bind('<Enter>', lambda e:root.configure(background='#0905f7'))
root.bind('<Leave>', lambda e:root.configure(background='#05f709'))

# Entry
entry1 = tk.Entry(root, font=('Arial', 16))
entry2 = tk.Entry(root, font=('Arial', 16))

entry1.bind('<FocusIn>', lambda e: entry1.configure(bg='cyan'))
entry1.bind('<FocusOut>', lambda e: entry1.configure(bg='coral'))
entry1.pack()
entry2.pack()



root.mainloop()
