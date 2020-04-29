
#Libraries
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import tkinter as tk
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from tkinter import filedialog


###---GLOBAL VARIABLES---###
root = Tk()

#variables for screen dimension
width_window = 350
height_window = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#variables who center the window on the computer screen
coordinate_x = (screen_width/2) - (width_window/2)
coordinate_y = (screen_height/2) - (height_window/2)


#Class of root window
class My_window(Frame):
    #Elements of the window
    # NUM_TOPIC = Spinbox()    #Spinbox for selct the topic number 
    eventButton = Button()
    exitButton = Button()
    goButton = Button()
    TopicListButton = Button()

    #Showing names option
    CheckVar = IntVar()
    NamesCheckButton = Checkbutton()

    #Labels of the window
    labelAlgorithm = Label()    #label for the algorithms
    label_spin = Label()        #label for the number of clusters

    labl1 = Label()             #empty label helping to build the interface
    labl2 = Label()             #empty label helping to build the interface
    labl3 = Label()             #empty label helping to build the interface
    labl4 = Label()             #empty label helping to build the interface
    labl5 = Label()             #empty label helping to build the interface
    labl6 = Label()             #empty label helping to build the interface
    labl7 = Label()             #empty label helping to build the interface
    labl8 = Label()             #empty label helping to build the interface
    labl9 = Label()             #empty label helping to build the interface
    labl10 = Label()            #empty label helping to build the interface

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.grid()
        self.PutWidgets()
        return

    #Exit of the app
    def Exit(self):
        exit()
        return


    def butnew(self, text, _class):

        self.goButton.config(text = text,command = lambda: self.new_window(_class))

        self.goButton.grid(row = 5, column = 2)

        return


    # def Error_window(self):

    #     self.new = Toplevel(self.master)
        
    #     self.new.geometry("250x100")

    #     lbl_error= Label(self.new, text="Please Select a Topic Number!")
    #     lbl_error.grid(row=0,column=0, padx=30,pady=20)

    #     return


    def new_window(self,_class):

        # num_topic = self.NUM_TOPIC.get()
        editable_names = self.CheckVar.get()
        root.filename =  filedialog.askdirectory()
        url_list = root.filename.split('/')
        folder_name = url_list[-1]
        print(folder_name)

        file_all_topics = open("C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.txt","r")

        for i in range(0, 135):

            line = file_all_topics.readline()            
            list_line = line.split()

            if(list_line[1] == folder_name):
                num_topic = list_line[0]
        
        


        # if(num_topic==''):
        #     self.Error_window()
        # else:
        self.new = Toplevel(self.master)
        # self.new.attributes('-fullscreen',True)
        self.new.geometry(str(screen_width+100) + 'x' + str(screen_height))
        # self.new.geometry("640x640")
        _class(self.new, num_topic ,editable_names,root.filename)

        return


    #init and put the widgets in the root window
    def PutWidgets(self):
        
        #labels for help to construct the interface
        self.labl1.config(text="      ")
        self.labl1.grid(row=0,column=1)

        self.labl2.config(text="      ")
        self.labl2.grid(row=0,column=2)

        self.labl3.config(text="      ")
        self.labl3.grid(row=1,column=1)

        self.labl4.config(text="      ")
        self.labl4.grid(row=1,column=2)

        self.labl5.config(text="      ")
        self.labl5.grid(row=2,column=1)

        self.labl6.config(text="      ")
        self.labl6.grid(row=2,column=2)

        self.labl7.config(text="      ")
        self.labl7.grid(row=2,column=0)

        # self.labl8.config(text="    ")
        # self.labl8.grid(row=5,column=1)

        self.labl9.config(text="     ")
        self.labl9.grid(row=4,column=1)

        # self.labl10.config(text="    ")
        # self.labl10.grid(row=4,column=2)


        # self.label_spin.config(text="Choose the topic (1 to 135)")
        # self.label_spin.grid(row=3,column=3)

        #spinbox to select number of clusters
        # self.NUM_TOPIC.config(from_=1, to=135)
        # self.NUM_TOPIC.grid(row=4,column=3)

        self.butnew("Choose Folder ", Win2)

        #topic list button
        self.TopicListButton.config(text="Topic List", command=self.TopicList)
        self.TopicListButton.grid(row=5, column=3)

        #Exit Button
        self.exitButton.config(text="Exit", command= self.Exit)
        self.exitButton.grid(row = 5, column = 4)


        self.NamesCheckButton.config(text="Editable Names", variable=self.CheckVar, onvalue=1, offvalue=0)
        self.NamesCheckButton.grid(row=4,column=2)

        return


    def TopicList(self):

        self.new = Toplevel(self.master)
        
        self.new.geometry("500x640")

        self.new.title("Topic List")

        self.grid()
        
        frame_canvas = Frame(self.new)
        frame_canvas.grid(row=0,column=0,columnspan=3)

        canvas = Canvas(frame_canvas, width=480, height=640,bg='green')
        canvas.grid(row=0,column=0)

        scrollbar = Scrollbar(frame_canvas,orient="vertical",command=canvas.yview)       
        scrollbar.grid(row=0, column=1, sticky='ns')

        canvas.configure(yscrollcommand=scrollbar.set)

        frame_labels = Frame(canvas)
        canvas.create_window(0,0,window=frame_labels, anchor='nw')

        file_topics_numbers = open("C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.txt","r")

        for i in range(0, 135):

            line = file_topics_numbers.readline()            
            list_line = line.split()
            lbl = Label(frame_labels, text="Topic"+str(i + 1) + ": "+ list_line[1])
            lbl.grid(row=i, column=0)


        frame_labels.update_idletasks()

        canvas.config(scrollregion=canvas.bbox("all"))


        return

##-- End of the class My_windows --##


#First Window Panel
class Win2():


    def __init__(self, master, num_topic,editable_names,folder_topic):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        #Colors
        Color_List = ['silver','rosybrown', 'lightcoral','navy', 'maroon', 'red', 'tomato','sienna','peru','darkorange',
                        'gold', 'olive', 'yellow','purple', 'yellowgreen', 'darkolivegreen','deeppink', 'lawngreen', 'lightgreen',
                        'mediumaquamarine', 'turquoise', 'paleturquoise', 'darkcyan','aqua','deepskyblue', 'steelblue', 
                        'dodgerblue', 'blueviolet','magenta', 'mediumvioletred',  'hotpink', 'crimson', 'pink']

        images_vector_url = self.Reading_folder_images(num_topic,folder_topic)
        images_vector_jpg =  self.ResizePhotos(images_vector_url)

        name_topic = self.FrameUP(num_topic,Color_List)
        self.FramesDown(images_vector_url,num_topic,name_topic,Color_List,editable_names,images_vector_jpg)
    

        return


    def ResizePhotos(self,url_vector):

        list_photo_type = []
        img_type = 0 

        for i in range(0, len(url_vector)):

            img = Image.open(url_vector[i])

            width,height = img.size

            if(width > height):#type == 1
                prop = width / 300
                height_prop = int(height / prop)
                img = img.resize((300,height_prop), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 1
                pack = [img_def,img_type]

            if(width < height):#type == 2
                prop = height / 300
                width_prop = int(width / prop)
                img = img.resize((185,300), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 2
                pack = [img_def,img_type]

            if(width == height):#type == 3
                img = img.resize((300,300), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 3
                pack = [img_def,img_type]

            list_photo_type.append(pack)


        return list_photo_type


    def Reading_folder_images(self,num_topic,folder_topic):

        self.a = "a\Hola"
        self.b = self.a[1]
        self.image_list = [] #images in PIL.JpegImagePlugin.JpegImageFile data type
        self.image_url = [] #images in str data type: url of the image in this computer

        for filename in glob.glob(folder_topic+"/*.jpg"):
            im=Image.open(filename)
            self.A = list(filename)
            i = 0
            for c in filename:
                if (c == self.b):
                    self.A[i] = '/'
                
                i = i +1
            self.image_url_def = self.listToString(self.A)
            self.image_url.append(self.image_url_def)
            self.image_list.append(ImageTk.PhotoImage(Image.open(self.image_url_def)))

        return (self.image_url)


    def Read_topics_file(self, num_topic):

        file_topics_numbers = open("C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.txt","r")

        list_topic = []

        for i in range(0, 134):

            line = file_topics_numbers.readline()            
            list_line = line.split()            
            list_topic.append(list_line[1])

        file_topics_numbers.close()

        name_topic = list_topic[int(num_topic) - 1]        

        return (name_topic)


    def FramesDown(self,images_vector,num_topic, name_topic,Color_List,editable_names,images_vector_jpg):
        
        
        #Frame para el canvas
        
        frame_canvas = Frame(self.frame)
        frame_canvas.grid(row=1, column=0, columnspan=5, sticky='nw')
       
        GENERAL_CANVAS = Canvas(frame_canvas,width=1510, height=750, bg='white')
        GENERAL_CANVAS.grid(row=0, column=0)

        scrollbar = Scrollbar(frame_canvas,orient="vertical",command=GENERAL_CANVAS.yview)       
        scrollbar.grid(row=0, column=1, sticky='ns')

        GENERAL_CANVAS.configure(yscrollcommand=scrollbar.set)

        frame_fotos = tk.Frame(GENERAL_CANVAS)
        GENERAL_CANVAS.create_window((0,0), window=frame_fotos, anchor='nw')
        
        
        # #Grid for the photos
        # #Every Folder has 300 photos, so we make a 60x5 grid
        rows = 61
        columns = 6

        frames_grid = [[Frame() for j in range(columns)] for i in range(rows)]
        canvas_grid = [[Canvas() for j in range(columns)] for i in range(rows)]

        _num_fotos = 0#contador para las fotos
        fotos_num = len(images_vector)

        self.images_vector_jpg = images_vector_jpg

        #Read rGT file
        list_similarity = self.ReadRGTFile(num_topic,name_topic,fotos_num)
        

        #Read dGT file
        list_clus_belong_photos = self.ReadDGTFile(num_topic,name_topic,fotos_num)


        #Read dclster GT file
        list_cluster_in_topic = self.ReadDclusterGT(num_topic,name_topic)


        for i in range (1, rows):

            _num_fotos += 1

            for j in range (1, columns):

                frames_grid[i][j] = Frame(frame_fotos)
                frames_grid[i][j].config(width=300,height=300)
                frames_grid[i][j].grid(row=i, column=j, sticky='n')

                if(_num_fotos <= fotos_num):

                    url_image = self.ExtractPhoto_fromUrl(images_vector[_num_fotos - 1])

                    canvas_grid[i][j] = Canvas(frames_grid[i][j], width=300, height=300)
                    canvas_grid[i][j].grid(row=0, column=0, columnspan=3)

                    self.pack = self.images_vector_jpg[_num_fotos-1]
                    self.img_type = self.pack[1] #ype of the image (size)
                    self.image = self.pack[0]


                    if(self.img_type == 1):#width > height
                            
                        canvas_grid[i][j].create_image(0,40, image=self.image, anchor='nw')

                    if(self.img_type == 2):#width < height
                        
                        canvas_grid[i][j].create_image(55,0, image=self.image, anchor='nw')

                    if(self.img_type == 3):#width == height
                        
                        canvas_grid[i][j].create_image(0,0, image=self.image, anchor='nw')

                    _lbl_number = tk.Label(frames_grid[i][j], text="IMAGE "+str(_num_fotos))    
                    _lbl_number.grid(row=1, column=0, sticky='s')


                    if(editable_names == 1):#True (Show photonames editable)

                        _photo_name = tk.Text(frames_grid[i][j], width=15, height=5)
                        _photo_name.grid(row=1, column=1, sticky='w')
                        _photo_name.insert(tk.END,url_image)

                    else:

                        _photo_name = Label(frames_grid[i][j], text=url_image)
                        _photo_name.grid(row=1, column=1, sticky='w')


                    _lbl_cluster = tk.Label(frames_grid[i][j])
                    _lbl_cluster.grid(row=1, column=2, sticky='w')

                    if(list_similarity[_num_fotos - 1] != '1'): #because in some folders there are '-1' instead of 0

                        canvas_grid[i][j].config(bg='white')            
                          
                        bckgrnd_lbl = 'red'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        _lbl_cluster.config(text="No Cluster", bg='black', fg='white')
                        
                        
                    else:                  
                    
                        #Background for the image                        
                        color_bckgrn,number_cluster = self.SetColorCluster(url_image,list_clus_belong_photos,Color_List)
                        canvas_grid[i][j].config(bg=color_bckgrn)

                        bckgrnd_lbl = 'green'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        # _lbl_cluster = tk.Label(frames_grid[i][j], text="Cluster "+str(number_cluster) + list_cluster_in_topic[int(number_cluster) - 1])
                        _lbl_cluster.config( text="Cluster "+str(number_cluster), bg=color_bckgrn)


                else:
                    canvas_grid[i][j] = Canvas(frames_grid[i][j], width=300, height=300, bg='black')                
                    canvas_grid[i][j].grid(row=0, column=0)
                    _lbl_number = tk.Label(frames_grid[i][j], text="IMAGE "+str(_num_fotos))
                    _lbl_number.grid(row=1, column=0, sticky='s')                           
                                        
                

                _num_fotos += 1

            _num_fotos -= 1

        #End loop For------------------

        frame_fotos.update_idletasks()        
          
        GENERAL_CANVAS.config(scrollregion=GENERAL_CANVAS.bbox("all"))

        return



    def SetColorCluster(self,url_image,list_clus_belong_photos,Color_List):

        #Search the image (url_image) in the list (list_clus_belong_photos)
        search = False
        size_list = len(list_clus_belong_photos)
        counter = 0
        while((counter < size_list) and (not search)):

            aux = list_clus_belong_photos[counter]
            image = aux[0]

            if(url_image == image):
                index = counter
                search = True

            counter += 1


        if(search):
            aux_ = list_clus_belong_photos[index]
            number_cluster = aux_[1]
            #Then associate the image with their color cluster
            color = Color_List[int(number_cluster) - 1]
        else:
            color = 'white'
            # number_cluster = 0


        return(color,number_cluster)


    def ExtractPhoto_fromUrl(self,url):

        url_list = url.split('/')
        img_with_jpg = url_list[-1]
        aux = img_with_jpg.split('.')
        img_ = aux[0]

        return (img_)


    def ReadRGTFile(self,num_topic,name_topic,number_objects):


        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/rGT/" + name_topic + " rGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/rGT/" + name_topic + " rGt.txt"


        rGT_file = open(filename, 'r')

        list_similarity = []

        for i in range(0, number_objects):

            line = rGT_file.readline()
            list_line = line.split()
            a = list_line[0]
            b = a[-1]
            list_similarity.append(b)

        rGT_file.close()

        return (list_similarity)


    def ReadDclusterGT(self,num_topic,name_topic):

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dclusterGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/dGT/" + name_topic + " dclusterGt.txt"
        

        dclusterGT_file = open(filename,'r')

        count = 0
        with open(filename, 'r') as f:
            for line in f:
                count += 1.

        list_cluster_topic = []

        for i in range(0, int(count)):

            line = dclusterGT_file.readline()
            list_line = line.split(',')               
            list_cluster_topic.append(list_line[1])


        dclusterGT_file.close()

        return (list_cluster_topic)


    def ReadDGTFile(self,num_topic,name_topic,number_objects):

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/dGT/" + name_topic + " dGt.txt"

        dGT_file = open(filename, 'r')

        list_clus_belong_photos = []

        count = 0
        with open(filename, 'r') as f:
            for line in f:
                count += 1.


        for i in range(0, int(count)):

            line = dGT_file.readline()
            list_line = line.split(',')
            photo_id = list_line[0]
            cluster_number = list_line[1]
            def_list = [photo_id, cluster_number]    
            list_clus_belong_photos.append(def_list)

        dGT_file.close()

        return (list_clus_belong_photos)


    def FrameUP(self,num_topic,Color_List):
        
        
        name_topic = self.Read_topics_file(num_topic)
        Label_Topic = Label(self.frame, text = "TOPIC "+ num_topic +": "+ name_topic) #cambiar tamaño y letra

        Button_Legend = Button(self.frame, text="Legend",command= lambda: self.LegendFrame(num_topic,name_topic,Color_List)) #meter listener que abra la otra ventana con los colors

        #Empty labels
        label_empty_1 = Label(self.frame, text="   ") #meterle marginsss
        label_empty_2 = Label(self.frame, text="   ")
        label_empty_3 = Label(self.frame, text="                ")

        
        Label_Topic.grid(row=0, column= 2)
        Button_Legend.grid(row=0, column = 4)
        label_empty_1.grid(row=0, column= 0)
        label_empty_2.grid(row=0, column= 1)
        label_empty_3.grid(row=0, column= 3)

        return (name_topic)

    
    def LegendFrame(self, num_topic,name_topic,Color_List):

        #container
        self.new = Toplevel(self.frame)        
        self.new.geometry("640x640")
        self.new.title("Legend Window")
        
        #Read dgt files
        list_cluster_in_topic = self.ReadDclusterGT(num_topic,name_topic)

        frame_canvas = Frame(self.new)
        frame_canvas.grid(row=0,column=0,columnspan=3)

        canvas = Canvas(frame_canvas, width=480, height=640)
        canvas.grid(row=0,column=0)

        scrollbar = Scrollbar(frame_canvas,orient="vertical",command=canvas.yview)       
        scrollbar.grid(row=0, column=1, sticky='ns')

        canvas.configure(yscrollcommand=scrollbar.set)

        frame_labels = Frame(canvas)
        canvas.create_window(0,0,window=frame_labels, anchor='nw')

        tam = len(list_cluster_in_topic)

        for i in range(0,tam):
            
            lbl = Label(frame_labels, text="Cluster "+str(i + 1) + ": "+ list_cluster_in_topic[i])
            lbl.grid(row=i, column=0, sticky='se')
            canvas_color = Canvas(frame_labels, height=30, bg=Color_List[i])
            canvas_color.grid(row=i,column=1)

        frame_labels.update_idletasks()

        canvas.config(scrollregion=canvas.bbox("all"))

        return


    def listToString(self,s):
        # initialize an empty string 
        str1 = ""

        # traverse in the string   
        for ele in s:  
            str1 += ele   
        
        # return string   
        return str1


root.geometry("%dx%d+%d+%d" % (width_window,height_window,coordinate_x,coordinate_y))

app = My_window(root)
app.mainloop()