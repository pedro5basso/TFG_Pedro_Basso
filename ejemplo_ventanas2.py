import tkinter as tk
from tkinter import *


class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.frame = Frame(self.master)
        self.butnew("Click to open Window 2", "2", Win2)
        self.frame.pack()


    def butnew(self, text, number, _class):
        Button(self.frame, text = text, command = lambda: self.new_window(number, _class)).pack()


    def new_window(self,number,_class):
        self.new = Toplevel(self.master)
        _class(self.new,number)
##-----------------------


class Win2:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("400x400+200+200")
        self.frame = Frame(self.master)
        self.quit = Button(self.frame, text = f"Quit this window n. {number}",command= self.close_window)
        self.quit.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()
         



root = Tk()
app = Win1(root)
root.mainloop()