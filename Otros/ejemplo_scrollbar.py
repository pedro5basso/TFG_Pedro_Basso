##### Ejemplo de imagen dentro del canvas
from tkinter import *
from PIL import ImageTk, Image

# create the canvas, size in pixels
canvas = Canvas(width=1510, height=750, bg='white')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file

url1='C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic77/topic77/8921676196.jpg' #ancho > alto
url2 = 'C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic77/topic77/9038530883.jpg' #ancho < alto
url3 = 'C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic77/topic77/12566067133.jpg' #ancho == alto 
img = Image.open(url2)
img = img.resize((170,300), Image.ANTIALIAS)
print(type(img))
gif1 = ImageTk.PhotoImage(img)
print(type(gif1))
# gif1 = ImageTk.PhotoImage(Image.open(url))

# gif2 = ImageTk.PhotoImage(Image.open('C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic97/topic97/9024389278.jpg'))

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
frame_fotos = Frame(canvas)
canvas.create_window(0,0, window=frame_fotos, anchor='nw')
canvas.create_image(0, 50, image=gif1, anchor=NW)
# canvas.create_image(400, 400, image=gif2, anchor=NW)

# run it ...
mainloop()
#-------------------------
#
# from tkinter import *
 ##### Ejemplo de Canvas dentro de Canvas
# class MainWindow(Frame):
#     def __init__(self):
#         super().__init__()
#         self.pack(expand=Y,fill=BOTH)

#         outercanvas = Canvas(self, width=200, height=100, bg='#00ffff')
#         outercanvas.pack(expand=Y,fill=BOTH)

#         innercanvas = Canvas(outercanvas, width=100, height=50)
#         outercanvas.create_window(50, 25, anchor=NW, window=innercanvas)

#         innercanvas.create_text(10, 10, anchor=NW, text="Hello")

# root = MainWindow()
# root.mainloop()


##--------------
##### Ejemplo del scrollbar
# from tkinter import *
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Scrolling")
# scrollbar = tk.Scrollbar(ventana)
# c = tk.Canvas(ventana,background='pink',yscrollcommand=scrollbar.set)
# scrollbar.config(command=c.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# elframe=tk.Frame(c)
# c.pack(side="left",fill="both",expand=True)
# c.create_window(0,0,window=elframe,anchor='nw')
# # texto= tk.Label(elframe,wraplength=500,
# # text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo. Pellentesque in consectetur felis, vel bibendum velit. Phasellus in magna vitae nisi tempus pulvinar. Quisque convallis vehicula luctus. Proin convallis vel enim vitae volutpat. Mauris luctus rutrum sapien, nec pellentesque eros auctor non. Cras urna urna, pharetra in auctor et, sollicitudin sed tortor. Nam lacinia, nunc sit amet dapibus placerat, metus turpis dapibus dui, sit amet convallis orci nibh et est. Aliquam erat volutpat.Nulla facilisi. Fusce at nunc nisl. Maecenas id ligula non est vestibulum consequat. Aenean eu augue massa. Morbi dignissim quis augue vel interdum. Mauris venenatis facilisis risus. Ut viverra, diam condimentum porttitor luctus, elit velit imperdiet urna, quis faucibus lacus libero ultrices lorem. Morbi malesuada at sem quis ullamcorper. In sit amet feugiat dolor, id accumsan diam. Aliquam erat volutpat. Cras id turpis euismod elit accumsan auctor. Donec tincidunt sagittis enim pretium ultricies. In dictum et mi laoreet mattis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat sem eget velit iaculis euismod. Sed eleifend orci quis velit rutrum, non cursus augue scelerisque. Aliquam iaculis erat et fringilla facilisis. Praesent facilisis mi eget tellus pharetra, sed condimentum massa varius. Fusce at lectus condimentum, suscipit mauris quis, ullamcorper ante. Etiam et feugiat arcu. Quisque et pellentesque justo.",
# # background="turquoise")
# # texto.pack()
# ventana.update()
# c.config(scrollregion=c.bbox("all"))
# ventana.mainloop()

# from tkinter import *

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )

# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )

# mainloop()