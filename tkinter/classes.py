from tkinter import *


class My_button:
    def __init__(self, master):
        self.printButton = Button(master, text='print', command=self.printMsg)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(master, text='Quit', command=master.quit)
        self.quitButton.pack(side=RIGHT)

    def printMsg(self):
        print("Printing msg")


root = Tk()
obj1 = My_button(root)
root.mainloop()
