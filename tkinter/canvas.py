from tkinter import *
root = Tk()
root.geometry('350x350+400+100')
# root.resizable(0, 0)

canvas1 = Canvas(root, width=300, height=100, bg="white")
canvas1.pack(expand=YES, fill=BOTH)

# line = canvas1.create_line(0, 0, 300, 150)
# redlone = canvas1.create_line(300, 150, 0, 300, fill="")

# arc = canvas1.create_arc(100, 100, 200, 200, extent=130)

photo = PhotoImage(file=r"img\img.png")
canvas1.create_image(0, 0, image=photo, anchor=NW)

# rectangle = canvas1.create_rectangle(100, 50, 200, 100, fill='yellow')

root.mainloop()
