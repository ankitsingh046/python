from tkinter import *
from tkinter import font, ttk

root = Tk()
root.minsize(350, 300)

my_font = font.Font(family="Arial",
                    size=16,
                    weight='bold',
                    slant='italic',  # roman
                    underline=1,  # 0
                    overstrike=1,  # 0
                    )

label = Label(root, text='Welcom Singh',
              # font=("Arial", 16, 'bold', 'italic', 'underline'),
              font=my_font,
              fg="coral"
              ).pack()

# list1 = []
# font_family = list(font.families())
# for item in font_family:
#     list1.append(item)

# combo1 = ttk.Combobox(root, values=list1).pack()


root.mainloop()
