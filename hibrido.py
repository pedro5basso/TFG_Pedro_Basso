import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import glob

root = tk.Tk()


def listToString(s):
    # initialize an empty string 
    str1 = ""

    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1



# def LoadImage

num_topic = str(77)
a = "a\Hola"
b = a[1]
image_url = [] #images in str data type: url of the image in this computer

for filename in glob.glob("C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic"+num_topic+"/topic"+num_topic+"/*.jpg"):
    im=Image.open(filename)
    A = list(filename)
    i = 0
    for c in filename:
        if (c == b):
            A[i] = '/'
        
        i = i +1
    image_url_def = listToString(A)
    image_url.append(image_url_def)



frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

# Add 9-by-5 buttons to the frame
rows = 61
columns = 6
# buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]


foto_grid  = [[tk.Canvas() for j in range(columns)] for i in range(rows)]
n_fotos=0

url1 = 'C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic77/topic77/173270475.jpg'
image1 = ImageTk.PhotoImage(Image.open(url1))

url2 = 'C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/topic77/topic77/2558753380.jpg'
image2 = ImageTk.PhotoImage(Image.open(url2))

for i in range(0, rows):
    # n_fotos += 1

    for j in range(0, columns):
        foto_grid[i][j] = tk.Canvas(frame_buttons, width=150, height=150, bg='green')
        foto_grid[i][j].grid(row=i, column=j, sticky='news')
        if(i % 2 == 0):
            # image1 = ImageTk.PhotoImage(Image.open(url1))
            foto_grid[i][j].create_image(0, 0, image= image1, anchor='nw')
        else:
            # image2 = ImageTk.PhotoImage(Image.open(url2))
            foto_grid[i][j].create_image(0, 0, image= image2, anchor='nw')

        # n_fotos += 1

    # n_fotos -= 1


# Update buttons frames idle tasks to let tkinter calculate buttons sizes
frame_buttons.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
first5columns_width = sum([foto_grid[0][j].winfo_width() for j in range(0, 5)])
first5rows_height = sum([foto_grid[i][0].winfo_height() for i in range(0,5)])
frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                    height=first5rows_height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))




root.mainloop()