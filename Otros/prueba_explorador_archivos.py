from tkinter import filedialog
from tkinter import *

root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
root.filename =  filedialog.askdirectory()
print (root.filename)