from tkinter import *
root = Tk()

# main menu
main_menu = Menu(root)
root.config(menu=main_menu)

# Menu items
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=edit_menu)

# Drop down menu items
file_menu.add_command(label="New", command=lambda: root.configure(background="black"))
file_menu.add_command(label="Open", command=lambda: root.configure(background="White"))
file_menu.add_separator()

# Drop down sub menu
save_menu = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Save", menu=save_menu)

# submenu items
save_menu.add_command(label="Save", command=lambda: root.configure(background="cyan"))
save_menu.add_command(label="Save As", command=lambda: root.configure(background="coral"))

root.mainloop()
