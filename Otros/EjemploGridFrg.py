from tkinter import *
from tkinter.ttk import *
import tkinter as tk


# def function(lbl):

#     lbl.grid_forget()
#     lbl.config(text="Nuevo Label")
#     lbl.grid(row=0, column=1)


#     return

# def function2(lbl):

#     lbl.grid_forget()
#     lbl.config(text="a")
#     lbl.grid(row=0, column=1)


#     return

# def main():

#     root = Tk()

#     root.title("proban2")
#     root.geometry("640x480")
#     root.grid()
#     lbl = Label(root)

#     lbl.config(text="Primera")
#     lbl.grid(row=0,column=0)


#     btt = Button(root, text="Borrar", command=lambda : function(lbl))
#     btt.grid(row=0,column=0)
#     btt = Button(root, text="Volver", command=lambda : function2(lbl))
#     btt.grid(row=1,column=0)
#     lbl.grid(row=0, column=1)

#     root.mainloop()

#     return

# main()

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

# label = Label(root)
# label.pack()
root.mainloop()