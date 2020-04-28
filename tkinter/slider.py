from tkinter import *

root = Tk()
root.minsize(320, 200)
root.title('slider')

s = Scale(root, from_=0, to=100, orient=HORIZONTAL, sliderlength=20,
          troughcolor="red")  # width, length,command,state,

s.pack(fill=X)

print(s.get())
root.mainloop()
