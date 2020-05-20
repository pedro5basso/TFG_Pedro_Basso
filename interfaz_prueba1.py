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
import webbrowser
import csv
import io


###---GLOBAL VARIABLES---###
root = Tk()

URL_IMAGES = 'C:/Users/Pedro/Desktop/TFG/Imagenes_TFG/'

#variables for screen dimension
width_window = 350
height_window = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#variables who center the window on the computer screen
coordinate_x = (screen_width/2) - (width_window/2)
coordinate_y = (screen_height/2) - (height_window/2)


# Class 1: Win1 
class Win1(Frame):


    def __init__(self, parent):
        
        Frame.__init__(self,parent) # init the frame
        self.parent = parent        # make the Frame the parent
        self.grid()                 # make it with grid structure
        self.PutWidgets()           # Call to PutWidgets() Function

        return


    def Exit(self):
        exit()
        return

    def PutWidgets(self):
        
        #Empty labels for help to construct the interface:

        lbl1 = Label(self.parent,text="      ")
        lbl1.grid(row=0,column=1)

        lbl2 = Label(self.parent,text="      ")
        lbl2.grid(row=0,column=2)

        lbl3 = Label(self.parent,text="      ")
        lbl3.grid(row=1,column=1)

        lbl4 = Label(self.parent,text="      ")
        lbl4.grid(row=1,column=2)

        lbl5 = Label(self.parent,text="      ")
        lbl5.grid(row=2,column=1)

        lbl6 = Label(self.parent,text="      ")
        lbl6.grid(row=2,column=2)

        lbl7 = Label(self.parent,text="      ")
        lbl7.grid(row=2,column=0)

        lbl8 = Label(self.parent,text="     ")
        lbl8.grid(row=4,column=1)


        # Check Results Button
        bttResults = Button(self.parent,text="Check Results",command=self.ResultsWindow)
        bttResults.grid(row = 5, column = 2)

        # Check Evaluations Button
        bttEvaluations = Button(self.parent,text="Check Evaluations", command=self.EvalWindow)
        bttEvaluations.grid(row=5, column=3)

        # Exit Button
        bttExit = Button(self.parent,text="Exit", command= self.Exit)
        bttExit.grid(row = 5, column = 4)

        
        return


    def ResultsWindow(self):

        tpl_result_window = Toplevel(self.master)
        tpl_result_window.title("Results Window")
        tpl_result_window.geometry("350x200")
        tpl_result_window.grid()
        Win3(tpl_result_window)


        return
        

    def EvalWindow(self):

        tpl_eval_window = Toplevel(self.master)
        tpl_eval_window.title("Evaluation Window")
        tpl_eval_window.geometry("350x200")
        tpl_eval_window.grid()
        Win4(tpl_eval_window)


        return

##-- End of Class 1: Win1 --##

# ------------------------------------------

# Class 2: Win2 
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

        list_images_url = self.Reading_folder_images(num_topic,folder_topic)
        list_images_resized =  self.ResizePhotos(list_images_url)

        name_topic = self.FrameUP(num_topic,Color_List)
        self.FramesDown(list_images_url,num_topic,name_topic,Color_List,editable_names,list_images_resized)
    

        return


    def ResizePhotos(self,list_url_images):

        list_photo_type = []
        img_type = 0 

        for i in range(0, len(list_url_images)):

            img = Image.open(list_url_images[i])

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

        self.a = "a\ "
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

        filename = "C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.txt"

        count = 0 
        with open(filename, 'r') as f:
            for line in f:
                count += 1.

        file_all_topics = open(filename,'r')

        list_topic = []

        for i in range(0, int(count)):

            line = file_all_topics.readline()            
            list_line = line.split()            
            list_topic.append(list_line[1])

        file_all_topics.close()

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
        fotos_num = len(images_vector) #cuantos elementos hay en el vector

        self.images_vector_jpg = images_vector_jpg

        #Read rGT file
        list_similarity = self.ReadRGTFile(num_topic,name_topic)
        

        #Read dGT file
        list_clus_belong_photos = self.ReadDGTFile(num_topic,name_topic)



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
                    self.img_type = self.pack[1] #type of the image (size)
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

                    sim = self.SearchSimilarity(url_image,list_similarity)
                    # print(sim_pack[0])

                    if(sim != 1):
                        # print(sim_pack[0])
                        # print("soy 0")

                        canvas_grid[i][j].config(bg='white')            
                            
                        bckgrnd_lbl = 'red'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        _lbl_cluster.config(text="No Cluster", bg='black', fg='white')   
                    else:
                        # print("soy 1")
                        #Background for the image                        
                        color_bckgrn,number_cluster = self.SetColorCluster(url_image,list_clus_belong_photos,Color_List)
                        canvas_grid[i][j].config(bg=color_bckgrn)

                        bckgrnd_lbl = 'green'
                        _lbl_number.config(bg=bckgrnd_lbl)

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


    def SearchSimilarity(self, url_image,list_similarity):

        search = False
        list_length = len(list_similarity)
        
        counter = 0

        while((counter < list_length) and (not search)):

            _pack = list_similarity[counter]
            # print(_pack)
            _photo_id = _pack[0]


            if(url_image == _photo_id):
                search = True
                if(int(_pack[1]) == 1):
                    sim = 1
                else:
                    sim = 0

            counter += 1




        return (sim)


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
        # else:
        #     color = 'white'
        #     # print("estoy mal")
        #     # print(url_image)
        #     number_cluster = 0


        return(color,number_cluster)


    def ExtractPhoto_fromUrl(self,url):

        url_list = url.split('/')
        img_with_jpg = url_list[-1]
        aux = img_with_jpg.split('.')
        img_ = aux[0]

        return (img_)


    def ReadRGTFile(self,num_topic,name_topic):


        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/rGT/" + name_topic + " rGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/rGT/" + name_topic + " rGt.txt"


        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            rGT_file = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            rGT_file = io.open(filename, 'r')


        list_similarity = []

        for i in range(0, int(count)):

            line = rGT_file.readline()
            list_line = line.split(',')
            photo_id = list_line[0]
            sim = list_line[-1]
            _pack = [photo_id,sim]
            list_similarity.append(_pack)
            # print(list_similarity[i],'\n')

        rGT_file.close()

        

        return (list_similarity)


    def ReadDclusterGT(self,num_topic,name_topic):

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dclusterGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/dGT/" + name_topic + " dclusterGt.txt"
        

        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            dclusterGT_file = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            dclusterGT_file = io.open(filename, 'r')

        list_cluster_topic = []

        for i in range(0, int(count)):

            line = dclusterGT_file.readline()
            list_line = line.split(',')               
            list_cluster_topic.append(list_line[1])


        dclusterGT_file.close()

        return (list_cluster_topic)


    def ReadDGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/dGT/" + name_topic + " dGt.txt"

        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            dGT_file = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            dGT_file = io.open(filename, 'r')

        list_clus_belong_photos = []

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

##-- End of Class 2: Win2 --##

# ------------------------------------------

# Class 3: Win3 
class Win3():
    
    CheckVar = IntVar()

    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.PutWidgets()  

        return


    def PutWidgets(self):        

        

        #Empty labels for help to construct the interface
        lbl1 = Label(self.master,text="      ")
        lbl1.grid(row=0,column=1)

        lbl2 = Label(self.master,text="      ")
        lbl2.grid(row=0,column=2)

        lbl3 = Label(self.master,text="      ")
        lbl3.grid(row=1,column=1)

        lbl4 = Label(self.master,text="      ")
        lbl4.grid(row=1,column=2)

        lbl5 = Label(self.master,text="      ")
        lbl5.grid(row=2,column=2)

        lbl6 = Label(self.master,text="      ")
        lbl6.grid(row=2,column=0)

        lbl7 = Label(self.master,text="      ")
        lbl7.grid(row=4,column=1)


       
        goButton = Button(self.master, text = "Choose Folder ",command = self.ResultsWindow)
        goButton.grid(row = 5, column = 2)


        #topic list button
        TopicListButton = Button(self.master,text="Topic List", command=self.TopicList)
        TopicListButton.grid(row=5, column=3)

        ExitButton = Button(self.master, text="Close", command = self.CloseWindow)
        ExitButton.grid(row=5, column=4)


        NamesCheckButton = Checkbutton(self.master,text="Editable Names", variable=self.CheckVar, onvalue=1, offvalue=0)
        NamesCheckButton.grid(row=4,column=2)


        return


    def ResultsWindow(self):

        # num_topic = self.NUM_TOPIC.get()
        editable_names = self.CheckVar.get()
        root.filename =  filedialog.askdirectory()
        url_list = root.filename.split('/')
        folder_name = url_list[-1]
        print(folder_name)

        if(folder_name != ''):

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
            Win2(self.new, num_topic ,editable_names,root.filename)
        else:
            print('Choose a folder!')

        return


    def CloseWindow(self):
        self.master.destroy()
        return


    def TopicList(self):

        self.new = Toplevel(self.master)
        
        self.new.geometry("500x640")

        self.new.title("Topic List")

        self.new.grid()
        
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

##-- End of Class 3: Win3 --##

# ------------------------------------------

# Class 4: Win4 
class Win4():


    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.PutWidgets()  

        return


    def PutWidgets(self):

        lbl_title_results = Label(self.master, text="Results File")
        lbl_title_results.grid(row=0,column=0)
        
        btt_selesct_file = Button(self.master, text="Select the Results file",command = self.CheckResultwindow)
        btt_selesct_file.grid(row=1,column=0)


        btt_close_window = Button(self.master, text="Close", command=self.CloseWindow)
        btt_close_window.grid(row=1,column=1)


        lbl_title_clusters = Label(self.master, text="Clusters File")
        lbl_title_clusters.grid(row=2,column=0)

        btt_clusters = Button(self.master, text="Select the Clusters file", command=self.CheckClustersWindow)
        btt_clusters.grid(row=3, column=0)


    def CloseWindow(self):

        self.master.destroy()

        return


    def CheckResultwindow(self):


        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Results file",filetypes = ((".txt files","*.txt"),("all files","*.*")))
        url_list = root.filename.split('/')
        file_txt_name = url_list[-1]
        # print(file_txt_name)

        if(file_txt_name != ''):          
            
            self.new = Toplevel(self.master)
            self.new.geometry(str(screen_width+100) + 'x' + str(screen_height))
            # self.new.geometry("640x640")
            self.new.grid()
            Win5(self.new,file_txt_name,root.filename)
        else:
            print('Choose a folder!')

        return


    def CheckClustersWindow(self):


        # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Cluster file",filetypes = ((".txt files","*.txt"),("all files","*.*")))
        # url_list = root.filename.split('/')
        # file_txt_name = url_list[-1]
        # self.new = Toplevel(self.master)
        # self.new.geometry(str(screen_width+100) + 'x' + str(screen_height))
        # # self.new.geometry("640x640")
        # self.new.grid()
        # Win6(self.new,file_txt_name,root.filename)
        

        new = 2
        url = "http://127.0.0.1:50537/index.html"
        webbrowser.open(url,new=new)


        return


##-- End of Class 4: Win4 --##

# ------------------------------------------

# Class 5: Win5
class Win5():

    def __init__(self, master,filename,path_filename):

        self.master = master
        self.frame = tk.Frame(self.master)

        # Leer el fichero
        # mostrar  fotos (basarse en la clase 2)
        result_list = self.ReadEvalFile(path_filename)

        num_topic,name_topic = self.Top_Frame(filename)
        self.Bottom_Frame(result_list,num_topic,name_topic)

        

        return

    def ReadEvalFile(self,path_filename):
        
        file_eval = open(path_filename, 'r')

        # counting the lines in the folder
        count = 0
        with open(path_filename, 'r') as f:
            for line in f:
                count += 1.

        
        #Example of a line of the file:

        # 77 0 3883881529 0 1.00 run5_relfeedback

        # first element (0): topic ID, number of the topic
        # second element (1): is ignored
        # third element (2): ID of the photo
        # fourth element (3): rank
        # fifth element (4): similarity
        # sixth element (5): name of the run

        list_result_eval = []

        for i in range(0, int(count)):

            line = file_eval.readline()
            list_line = line.split(' ')
            number_topic = list_line[0] #to save the topic number
            id_photo = list_line[2] #to save the ID photo
            # rank_photo = list_line[3] #to save the rank of the photo --> index of the vector
            sim_photo = list_line[4] #to save the sim of the photo
            # def_list = [number_topic,id_photo,rank_photo,sim_photo]
            def_list = [number_topic,id_photo,sim_photo]
            list_result_eval.append(def_list)


        file_eval.close()

        return list_result_eval

    def Top_Frame(self,filename):


        # 1: estraer el número del fichero para saber el tópico
        num_topic = self.Extract_Number_of_filename(filename)
        # print(num_topic)

        # 2: Relacionar con el nombre del tópico, para poder acceder a la carpeta de las fotos
        name_topic = self.NameTopic(num_topic)

        lbl_filename = Label(self.master, text="FILE SELECTED: " + filename) #cambiar tamaño y letra
        lbl_filename.grid(row=0,column=1)


        lbl_topic_info = Label(self.master, text="Topic "+num_topic + ": "+ name_topic )
        lbl_topic_info.grid(row=0,column=3)


        btt_close_window = Button(self.master, text="Close", command=self.CloseWindow)
        btt_close_window.grid(row=0,column=4)

        
        return(num_topic,name_topic)

    def CloseWindow(self):

        self.master.destroy()

        return

    def Bottom_Frame(self,result_list,num_topic,name_topic):

        # Misma estructura que la clase 2

        
        # print(name_topic)
        
        list_rgt = self.ReadRGTFile(num_topic,name_topic)

        list_dgt = self.ReadDGTFile(num_topic,name_topic)
        
        # print(len(list_rgt))

        # Make 1 list with the only 50 photos of the result
        list_50_images = self.Make50ImagesList(result_list,name_topic)

        # resize de las imagenes:
        list_resized_photos =  self.ResizePhotos(list_50_images)


        list_sim_50_photos,number_of_ones,AP_list = self.Make50similarityList(list_rgt,result_list)
        # print(len(list_sim_50_photos))

        num_of_clusters = self.ReadDclusterGT(num_topic,name_topic)
        
        list_clust_50 = self.Make50ClusterList(list_dgt,result_list)
        # print(len(list_clust_50))
        list_n_times_clust = self.MakeList_Compute_ClusterR(list_clust_50)
        # print(len(list_clust_50))
        


        self.MakeBotFrame(num_topic, name_topic,list_resized_photos,list_sim_50_photos,number_of_ones,AP_list,num_of_clusters,list_n_times_clust)


        return


    def MakeList_Compute_ClusterR(self,list_clust_50):

        # example input: [6,1,11,6,6,4,6,4,4,4]
        # example output: [1,2,3,3,3,4,4,4,4]

        def_list = []
        aux_list = []
        cont = 1
        def_list.append(cont)
        aux_list.append(list_clust_50[0])
        i = 1
        search = False
        muestra = list_clust_50[0]
        while( i < len(list_clust_50)):
            
            aux_list.append(muestra)

            if(aux_list.count(list_clust_50[i]) == 0):
                cont +=1
                
            muestra = list_clust_50[i]

            def_list.append(cont)
            i += 1


        return(def_list)


    def Make50similarityList(self,list_rgt,result_list):
        
        # 1-extract every photo_id of result_list and check if it is relevant or not
        # 2-count all relevant photos in the solution file
        # 3-compute precision and recall

        list_50_img_similarity = []
        search = False
        size_list_examinations = len(result_list)
        size_list_solutions = len(list_rgt)
        count_1 = 0
        count_2 = 0
        number_of_ones = 0
        AP_list = []

        while(count_1 < size_list_examinations):
            
            pack_0 = result_list[count_1]
            img_ex_file = pack_0[1]  #extract the photo from the examination folder
            count_2 = 0
            search = False
               

            while( (count_2 < size_list_solutions) and (not search)):

                pack_ = list_rgt[count_2]
                img_sol_file = pack_[0] # extract the image of the solution file
                
                
                if(img_ex_file == img_sol_file): # the image are equal
                    
                    search = True
                    sim = int(pack_[1]) # extract the similarity of rGT folder             

                    if(sim == 0):
                        pack_3 = [img_ex_file,'0']
                        list_50_img_similarity.append(pack_3)
                        AP_list.append(0)
                    else:
                        number_of_ones += 1
                        pack_3 = [img_ex_file,'1']
                        list_50_img_similarity.append(pack_3)
                        AP_list.append(1)

                               
                count_2 += 1
            
            count_1 += 1

        
        return(list_50_img_similarity,number_of_ones,AP_list)



    def Make50ClusterList(self,list_dgt,result_list):

        list_50_clust = []
        search = False
        size_list_examinations = len(result_list)
        
        size_list_solutions = len(list_dgt)
        count_1 = 0
        count_2 = 0

        while(count_1 < size_list_examinations):  

            pack_0 = result_list[count_1]
            img_ex_file = pack_0[1]  #extract the photo from the examination folder
            count_2 = 0
            search = False   

            while( (count_2 < size_list_solutions) and (not search)):

                pack_ = list_dgt[count_2]
                img_sol_file = pack_[0] # extract the image of the solution file
                
                if(img_ex_file == img_sol_file): # the image are equal

                    search = True
                    clust = (pack_[1]) # extract the cluster of dGT folder
                    list_50_clust.append(clust)

                             
                count_2 += 1


            count_1 += 1

        # print(len(list_50_clust))
        return(list_50_clust)




    def ReadDGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/dGT/" + name_topic + " dGt.txt"

        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            dGT_file = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            dGT_file = io.open(filename, 'r')

        list_clus_belong_photos = []

        for i in range(0, int(count)):

            line = dGT_file.readline()
            list_line = line.split(',')
            photo_id = list_line[0]
            cluster_number = list_line[1]
            def_list = [photo_id, cluster_number]    
            list_clus_belong_photos.append(def_list)

        dGT_file.close()

        return (list_clus_belong_photos)

    def ReadDclusterGT(self,num_topic,name_topic):

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dclusterGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/dGT/" + name_topic + " dclusterGt.txt"
        

        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            dclusterGT_file = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            dclusterGT_file = io.open(filename, 'r')

        list_cluster_topic = []

        for i in range(0, int(count)):

            line = dclusterGT_file.readline()
            list_line = line.split(',')               
            list_cluster_topic.append(list_line[0])



        dclusterGT_file.close()

        return (len(list_cluster_topic))


    def Make50ImagesList(self,result_list,name_topic):

        list_images_50 = []
        search = False
        size_list = len(result_list)
        counter = 0

        for i in range(0,size_list):

            _pack = result_list[i]
            id_photo_result = _pack[1]
            image_path = URL_IMAGES + name_topic + "/" + id_photo_result + ".jpg"

            list_images_50.append(image_path)


        return(list_images_50)


    def MakeBotFrame(self,num_topic, name_topic,list_resized_photos,list_sim_50_photos,number_of_ones,AP_list,num_of_clusters,list_n_times_clust):


        precission_list = []
        Clust_Recall_list = []
        Cust_recall_graphic_list = []
        F1_score_list = []
        cont_aux = 0
        #Frame para el canvas
        
        frame_canvas = Frame(self.master)
        frame_canvas.grid(row=1, column=0, columnspan=5, sticky='nw')
       
        GENERAL_CANVAS = Canvas(frame_canvas,width=1510, height=750, bg='white')
        GENERAL_CANVAS.grid(row=0, column=0)

        scrollbar = Scrollbar(frame_canvas,orient="vertical",command=GENERAL_CANVAS.yview)       
        scrollbar.grid(row=0, column=1, sticky='ns')

        GENERAL_CANVAS.configure(yscrollcommand=scrollbar.set)

        frame_fotos = tk.Frame(GENERAL_CANVAS)
        GENERAL_CANVAS.create_window((0,0), window=frame_fotos, anchor='nw')


        # #Grid for the photos
        
        rows = 11
        columns = 6

        frames_grid = [[Frame() for j in range(columns)] for i in range(rows)]
        canvas_grid = [[Canvas() for j in range(columns)] for i in range(rows)]

        _num_fotos = 0#contador para las fotos
        fotos_num = len(list_resized_photos)

        self.images_vector_jpg = list_resized_photos
        

        total_sim = 0

        for i in range (1, rows):

            _num_fotos += 1
            cont_aux += 1

            for j in range (1, columns):

                frames_grid[i][j] = Frame(frame_fotos)
                frames_grid[i][j].config(width=300,height=300)
                frames_grid[i][j].grid(row=i, column=j, sticky='n')

                if(_num_fotos <= fotos_num):

                    _pack_name = list_sim_50_photos[_num_fotos - 1]
                    _name = _pack_name[0]

                    sim = _pack_name[1]
                    total_sim += int(sim)

                    precision = total_sim / (_num_fotos)
                    precission_list.append(precision)

                    recall = total_sim / number_of_ones


                    precison_2_decimals = "%.4f" % precision
                    recall_2_decimals = "%.4f" % recall
                    
                    
                    lbl_precision = Label(frames_grid[i][j], text="P@" + str(_num_fotos) + "= " + str(precison_2_decimals) )
                    lbl_precision.grid(row=1, column=1, sticky='w')

                    lbl_recall = Label(frames_grid[i][j], text="R= " + str(recall_2_decimals))
                    lbl_recall.grid(row=1,column=2, sticky='w')

                    _pack_sim = list_sim_50_photos[_num_fotos - 1]
                    sim_image = _pack_sim[1]

                    if(sim_image == '1'):

                        bg_color='green'

                        CR = list_n_times_clust[cont_aux -1] / num_of_clusters
                        Clust_Recall_list.append(CR)
                        
                        F1 = 2*((precision * CR)/(precision + CR))
                        # F1_score_list.append(F1)
                        

                    else:
                        bg_color='red'
                        if(len(Clust_Recall_list) == 0):
                            CR = 0
                            F1 = 0
                        else:
                            # print(_num_fotos)
                            # print(len(Clust_Recall_list))
                            CR = Clust_Recall_list[-1]
                            F1 = 2*((precision * CR)/(precision + CR))
                        # Clust_Recall_list.append(CR)

                        cont_aux -= 1


                    #for graphics
                    Cust_recall_graphic_list.append(CR)
                    F1_score_list.append(F1)


                    F1_2_decimals = "%.4f" % F1
                    lbl_F1 = Label(frames_grid[i][j], text="F1@" + str(_num_fotos) + "= "+ str(F1_2_decimals))
                    lbl_F1.grid(row=2,column=1)

                    CR_2_decimals = "%.4f" % CR
                    lbl_CR = Label(frames_grid[i][j], text = "CR@" + str(_num_fotos) + "= "+ str(CR_2_decimals))
                    lbl_CR.grid(row=2,column=2)


                    _lbl_number = tk.Label(frames_grid[i][j], text="ID: " + _name)
                    _lbl_number.config(bg=bg_color)
                    _lbl_number.grid(row=1, column=0, sticky='s')

                    canvas_grid[i][j] = Canvas(frames_grid[i][j], width=300, height=300,bg=bg_color)
                    canvas_grid[i][j].grid(row=0, column=0, columnspan=4)

                    self.pack = self.images_vector_jpg[_num_fotos-1] 
                    self.img_type = self.pack[1] #type of the image (size)
                    self.image = self.pack[0]


                    if(self.img_type == 1):#width > height
                            
                        canvas_grid[i][j].create_image(0,40, image=self.image, anchor='nw')

                    if(self.img_type == 2):#width < height
                        
                        canvas_grid[i][j].create_image(55,0, image=self.image, anchor='nw')

                    if(self.img_type == 3):#width == height
                        
                        canvas_grid[i][j].create_image(0,0, image=self.image, anchor='nw')


                else:
                    canvas_grid[i][j] = Canvas(frames_grid[i][j], width=300, height=300, bg='black')                
                    canvas_grid[i][j].grid(row=0, column=0)
                    _lbl_number = tk.Label(frames_grid[i][j], text="IMAGE "+str(_num_fotos))
                    _lbl_number.grid(row=1, column=0, sticky='s')                           
                                        
                

                _num_fotos += 1
                cont_aux += 1

            _num_fotos -= 1
            cont_aux -= 1

        AP_def = self.Calculate_AP(precission_list,AP_list,number_of_ones)

        lbl_AP = Label(self.master, text = "AP@"+str(_num_fotos)+"= "+ str(AP_def))
        lbl_AP.grid(row=2,column=0)

        btt_graphics = Button(self.master, text="Graphics", command= lambda: self.MakeGraphics(precission_list,Cust_recall_graphic_list,F1_score_list))
        btt_graphics.grid(row=2,column=2)

        btt_pie_chart = Button(self.master, text="Pie Chart Similarity", command= lambda: self.MakePieChart(precission_list,number_of_ones))
        btt_pie_chart.grid(row=2,column=3)

        
        # print(len(precission_list))
        # print(len(F1_score_list))
        # print(len(Cust_recall_graphic_list))
        #End loop For------------------

        
        frame_fotos.update_idletasks()        
          
        GENERAL_CANVAS.config(scrollregion=GENERAL_CANVAS.bbox("all"))

        return


    def MakePieChart(self,precission_list,number_of_ones):

        # Data to plot
        labels = 'Similarity', 'No Similarity'
        num_0 = len(precission_list) - number_of_ones
        sizes = [number_of_ones, num_0]
        colors = ['green', 'red']
        explode = (0, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)

        plt.axis('equal')
        plt.show()


        return


    def MakeGraphics(self,precission_list,Cust_recall_graphic_list,F1_score_list):

        X_axis_list = list(range(0,len(precission_list)))


        # Create plots with pre-defined labels.
        fig, ax = plt.subplots()
        ax.plot(X_axis_list, precission_list, 'k',color='red', label='Precission')
        ax.plot(X_axis_list, Cust_recall_graphic_list, 'k',color='blue', label='Cluster Recall')
        ax.plot(X_axis_list, F1_score_list, 'k', color='green', label='F1 Score')

        # Shrink current axis's height by 10% on the bottom
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                fancybox=True, shadow=True, ncol=5)

        plt.show()


        return



    def Calculate_AP(self,precission_list,AP_list,number_of_ones):

        AP = 0
        total_sum_prod = 0
        _prod = 0

        for i in range(0,len(precission_list)):

            _prod = precission_list[i] * AP_list[i]

            total_sum_prod += _prod
        
        AP = (total_sum_prod / number_of_ones)
        AP_def = "%.3f" % AP

        return(AP_def)


    def Extract_Number_of_filename(self, filename):

        
        # 3 posibilities of filename:

        #  1-9,  one number
        #   MediaEval16_UNED_relfeedback8.txt

        # 10-99, two numbers
        #   MediaEval16_UNED_relfeedback78.txt


        # 100-135, three numbers
        #   MediaEval16_UNED_relfeedback101.txt
        

        units = filename[-5] #extract the units

        try:
            tens = filename[-6] #extract the tens in case the topic is between 10 and 99
            int_tens = int(tens)
            num_topic = tens + units
            aux_1_number = False
        except:
            # print("Only 1 digit")
            ten_topics = ''
            num_topic = units
            aux_1_number = True

        try:
            hundreds = filename[-7] #extract the tens in case the topic is between 100 and 135
            int_hundreds = int(hundreds)
            num_topic = hundreds + tens + units
        except:
            # print("Only 2 Digits")
            hundred = ''
            if(aux_1_number):
                num_topic =  units
            else:
                num_topic = tens + units


        return(num_topic)



    def ReadRGTFile(self,num_topic,name_topic):

        

        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/rGT/" + name_topic + " rGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/rGT/" + name_topic + " rGt.txt"


        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            rGT_file = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            rGT_file = io.open(filename, 'r')
        

        list_similarity = []

        for i in range(0, int(count)):

            line = rGT_file.readline()
            list_line = line.split(',')
            phoyo_id = list_line[0]
            similarity = list_line[-1]
            def_list = [phoyo_id,similarity]
            list_similarity.append(def_list)

        rGT_file.close()


        return (list_similarity)




    def NameTopic(self, num_topic):

        file_topics_numbers = open("C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.txt","r")

        list_topic = []

        for i in range(0, 134):

            line = file_topics_numbers.readline()            
            list_line = line.split()            
            list_topic.append(list_line[1])

        file_topics_numbers.close()

        name_topic = list_topic[int(num_topic) - 1]        

        return (name_topic)


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

##-- End of Class 5: Win5 --##

# ------------------------------------------

# Class 6: Win6
class Win6():

    def __init__(self, master,file_txt_name,file_path):

        self.master = master
        self.frame = tk.Frame(self.master)

        name_topic,num_topic = self.Extract_Name_Number_Topic(file_txt_name)
        
        list_clus_belong_photos = self.ReadClustersFile(file_path)
        
        list_clus_belong_real_photos = self.ReadDGTFile(name_topic,num_topic,file_path)

        # list_resized_photos =  self.ResizePhotos(list_clus_belong_real_photos,name_topic)

        # self.SetImagesClusterFile(name_topic,list_clus_belong_photos,list_resized_photos)
        

        
        return
    

    def ReadClustersFile(self,file_path):

        # print(file_path)
        # print(type(file_path))

        cluster_file = open(file_path, 'r')

        list_clus_belong_photos = []

        count = 0
        with open(file_path, 'r') as f:
            for line in f:
                count += 1.

        #Read the first line, that is text
        line = cluster_file.readline()

        for i in range(0, int(count) - 1):

            line = cluster_file.readline()
            list_line = line.split('\t')
            # print(list_line)
            photo_id = list_line[0]
            cluster_number = list_line[1]
            def_list = [photo_id, cluster_number]    
            list_clus_belong_photos.append(def_list)

        cluster_file.close()

        return (list_clus_belong_photos)


    def Extract_Name_Number_Topic(self,file_txt_name):


        list_name_file = file_txt_name.split('-')
        num_topic = list_name_file[0]
        name_topic = list_name_file[1]


        return (name_topic, num_topic)


    def ReadDGTFile(self,name_topic,num_topic,file_path):


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

##-- End of Class 6: Win6 --##

# ------------------------------------------

root.geometry("%dx%d+%d+%d" % (width_window,height_window,coordinate_x,coordinate_y))

app = Win1(root)
app.mainloop()