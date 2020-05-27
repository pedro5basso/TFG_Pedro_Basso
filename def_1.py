#Libraries
import tkinter as tk
import glob
import numpy as np
import matplotlib.pyplot as plt
import webbrowser
import csv
import io
import shutil
import socketserver
import socket
import sys

from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from matplotlib import colors as mcolors
from tkinter import filedialog


###---GLOBAL VARIABLES---###
root = Tk()

URL_IMAGES = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/Imagenes_TFG/'
URL_D3_FILES = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/'

#variables for screen dimension
width_window = 400
height_window = 190

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#variables who center the window on the computer screen
coordinate_x = (screen_width/2) - (width_window/2)
coordinate_y = (screen_height/2) - (height_window/2)


# Class 1: Win1 
class Win1(Frame):

    _frame1 = Frame()
    _frame2 = Frame()
    CheckVarEditable = IntVar()
    CheckVarClusters = IntVar()

    def __init__(self, parent):
        
        Frame.__init__(self,parent) # init the frame
        self.parent = parent        # make the Frame the parent
        self.grid()                 # make it with grid structure
        self._frame1 = Frame(self.parent)
        self._frame2 = Frame(self.parent)
        self.PutWidgets()           # Call to PutWidgets() Function

        return

    def PutWidgets(self):
        
        self._frame1.grid(row=0,column=0)

        self._frame2.grid(row=0,column=1)

        lbl1 = Label(self._frame1,text="      ")
        lbl1.grid(row=0,column=0)

        lbl2 = Label(self._frame1,text="      ")
        lbl2.grid(row=1,column=0)

        lbl3 = Label(self._frame1,text="      ")
        lbl3.grid(row=2,column=0)

        lbl4 = Label(self._frame1,text="      ")
        lbl4.grid(row=3,column=0)

        lbl5 = Label(self._frame1,text="      ")
        lbl5.grid(row=3,column=1)

        lbl6 = Label(self._frame1,text="      ")
        lbl6.grid(row=5,column=2)

        var = IntVar()
        R1 = Radiobutton(self._frame1, text="Check Results", variable=var, value=1, command= lambda: self.setFrame(var))
        R1.grid(row=3,column=2,sticky='w')

        R2 = Radiobutton(self._frame1, text="Check Evaluations", variable=var, value=2, command= lambda: self.setFrame(var))
        R2.grid(row=4,column=2,sticky='w')

        bttExit = Button(self._frame1,text="Exit", command= self.Exit)
        bttExit.grid(row = 6, column = 2,sticky='w')
 
        return

    def setFrame(self,var):

        if(var.get() == 1):                     
            self.MakeResultsPart()

        if(var.get() == 2):                       
            self.MakeEvalPart()
            
        return

    def MakeResultsPart(self):
        
        self._frame2.grid_forget()
        self._frame2 = Frame(self.parent)
        self._frame2.grid(row=0,column=1)

        lbl1 = Label(self._frame2,text="      ")
        lbl1.grid(row=0,column=0)

        lbl2 = Label(self._frame2,text="      ")
        lbl2.grid(row=1,column=0)

        goButton = Button(self._frame2, text = "Choose Folder ",command = self.ResultsWindow)
        goButton.grid(row = 5, column = 3)

        TopicListButton = Button(self._frame2,text="Topic List", command=self.TopicList)
        TopicListButton.grid(row=5, column=4)
 
        NamesCheckButton = Checkbutton(self._frame2,text="Editable Names", variable=self.CheckVarEditable, onvalue=1, offvalue=0)
        NamesCheckButton.grid(row=6,column=3,sticky='w')

        ClusterCheckButton = Checkbutton(self._frame2,text="Order by Cluster", variable=self.CheckVarClusters, onvalue=1, offvalue=0)
        ClusterCheckButton.grid(row=7,column=3,sticky='w')

        return

    def ResultsWindow(self):

        editable_names = self.CheckVarEditable.get()
        order_clusters = self.CheckVarClusters.get()
        root.filename =  filedialog.askdirectory()
        
        url_list = root.filename.split('/')
        folder_name = url_list[-1]

        if(folder_name != ''):

            file_all_topics = open("C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.txt","r")

            for i in range(0, 135):

                line = file_all_topics.readline()            
                list_line = line.split()

                if(list_line[1] == folder_name):
                    num_topic = list_line[0]
            
            self.new = Toplevel(self.master)
            self.new.geometry(str(screen_width+100) + 'x' + str(screen_height))
            Win2(self.new, num_topic ,editable_names,root.filename,order_clusters)
        else:
            print('Choose a folder!')

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

    def MakeEvalPart(self):
        
        self._frame2.grid_forget()
        self._frame2 = Frame(self.parent)
        self._frame2.grid(row=0,column=1)

        lbl1 = Label(self._frame2,text="      ")
        lbl1.grid(row=0,column=0)

        lbl2 = Label(self._frame2,text="      ")
        lbl2.grid(row=1,column=0)

        lbl3 = Label(self._frame2,text="      ")
        lbl3.grid(row=0,column=1)

        lbl3 = Label(self._frame2,text="      ")
        lbl3.grid(row=3,column=1)
        

        lbl_title_results = Label(self._frame2, text="Results File")
        lbl_title_results.grid(row=1,column=1)
        
        btt_selesct_file = Button(self._frame2, text="Select the Results file",command = self.CheckResultwindow)
        btt_selesct_file.grid(row=2,column=1)

        lbl_title_clusters = Label(self._frame2, text="Clusters File")
        lbl_title_clusters.grid(row=4,column=1)
        
        btt_clusters = Button(self._frame2, text="Select the Clusters file", command=self.CheckClustersWindow)
        btt_clusters.grid(row=5, column=1)

        return

    def CheckResultwindow(self):


        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Results file",filetypes = ((".txt files","*.txt"),("all files","*.*")))
        url_list = root.filename.split('/')
        file_txt_name = url_list[-1]

        if(file_txt_name != ''):          
            
            self.new = Toplevel(self.master)
            self.new.geometry(str(screen_width+100) + 'x' + str(screen_height))
            self.new.grid()
            Win5(self.new,file_txt_name,root.filename)
        else:
            print('Choose a folder!')

        return   

    def CheckClustersWindow(self):


        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Cluster file",filetypes = ((".txt files","*.txt"),("all files","*.*")))
        url_list = root.filename.split('/')
        file_txt_name = url_list[-1]

        self.MakeSpecificFiles(file_txt_name,root.filename)

        return

    def MakeSpecificFiles(self,file_txt_name,filename_path):

        name_topic,num_topic = self.Extract_Name_Number_Topic(file_txt_name)
        
        self.MakeSpecificTitletopic(name_topic,num_topic)

        list_dgt = self.MakeSpecificdGTFile(name_topic,num_topic)

        self.MakeSpecificdClusterFile(name_topic,num_topic)

        self.MakeSecificSelectedFile(filename_path,list_dgt)

        self.RunHtml()

        return

    def Extract_Name_Number_Topic(self,file_txt_name):

        list_name_file = file_txt_name.split('-')
        num_topic = list_name_file[0]
        name_topic = list_name_file[1]

        return (name_topic, num_topic)

    def MakeSpecificTitletopic(self,name_topic,num_topic):

        FILE_TO_MODIFY = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/titletopic.txt'

        list_file = str(num_topic)+','+name_topic

        with open(FILE_TO_MODIFY, 'w') as f:
            for item in list_file:
                f.write("%s" % item)

        src=open(FILE_TO_MODIFY,"r")
        fline="NUM_TOPIC,NAME_TOPIC\n"
        oline=src.readlines()
        oline.insert(0,fline)
        src.close()
        
        src=open(FILE_TO_MODIFY,"w")
        src.writelines(oline)
        src.close()

        return

    def MakeSpecificdGTFile(self,name_topic,num_topic):

        FILE_TO_MODIFY = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/filedGT.txt'

        list_file = self.ReadDGTFile(num_topic,name_topic)

        with open(FILE_TO_MODIFY, 'w') as f:
            for item in list_file:
                f.write("%s" % item)

        src=open(FILE_TO_MODIFY,"r")
        fline="ID_Photo,ID_Cluster\n"
        oline=src.readlines()
        oline.insert(0,fline)
        src.close()
        
        src=open(FILE_TO_MODIFY,"w")
        src.writelines(oline)
        src.close()

        return(list_file)

    def ReadDGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dGt.txt"
        else:
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
        list_clus_belong_photos = []


        for i in range(0, int(count)):

            line = dGT_file.readline()
    
            list_line = line.split(',')                  
            photo_id = list_line[0]             
            cluster_number = list_line[1]
            def_list = photo_id+','+cluster_number
            list_clus_belong_photos.append(def_list)
            
        dGT_file.close()

        return (list_clus_belong_photos)

    def MakeSpecificdClusterFile(self,name_topic,num_topic):

        FILE_TO_MODIFY = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/filedclusterGT.txt'

        list_file = self.ReadDclusterGT(num_topic,name_topic)

        with open(FILE_TO_MODIFY, 'w') as f:
            for item in list_file:
                f.write("%s" % item)

        src=open(FILE_TO_MODIFY,"r")
        fline="Cluster_Number,Cluster_Name\n"
        oline=src.readlines()
        oline.insert(0,fline)
        src.close()
        
        src=open(FILE_TO_MODIFY,"w")
        src.writelines(oline)
        src.close()

        return

    def ReadDclusterGT(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dclusterGt.txt"
        else:
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
            number = list_line[0]
            name =  list_line[1]
            def_list = number+','+name
            list_cluster_topic.append(def_list)
            
    
        dclusterGT_file.close()

        return (list_cluster_topic)

    def MakeSecificSelectedFile(self,filename_path,list_dgt):

        list_clusters = self.BuildClusterDefFile(filename_path,list_dgt)

        FILE_TO_MODIFY = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/combinedClusterFile.txt'

        with open(FILE_TO_MODIFY, 'w') as f:
            for item in list_clusters:
                f.write("%s" % item)

        src=open(FILE_TO_MODIFY,"r")
        fline="ID_Photo,ID_RCluster,ID_ECluster\n"
        oline=src.readlines()
        oline.insert(0,fline)
        src.close()
        
        src=open(FILE_TO_MODIFY,"w")
        src.writelines(oline)
        src.close()
        
        old_path = filename_path
        path_new = URL_D3_FILES + 'fileClusters.txt'

        shutil.copy(old_path, path_new)

        return

    def BuildClusterDefFile(self,filename_path,list_dgt):

        list_examination_cluster = self.ReadClusterFile(filename_path)

        size_list_solution = len(list_dgt)
        size_list_ex = len(list_examination_cluster)
        counter1 = 0
        
        def_list_cluster = []

        while(counter1 < size_list_solution):

            comb_r = list_dgt[counter1]
            comb_r_ = comb_r.split(',')
            id_photo_r = comb_r_[0]
            id_cluster_r = int(comb_r_[-1])

            search = False
            counter2 = 1

            while((counter2 < size_list_ex) and (not search)):
                
                comb_e = list_examination_cluster[counter2]
                id_photo_e = comb_e[0]
                if(int(id_photo_r) == int(id_photo_e)):
                    id_cluster_e = comb_e[1]                  
                    def_list = id_photo_r+','+str(id_cluster_r)+','+id_cluster_e
                    def_list_cluster.append(def_list)
                    search = True

                counter2 += 1
            
            counter1 += 1

        return(def_list_cluster)

    def ReadClusterFile(self,filename):

        try:
            count = 0 
            with io.open(filename, 'r', encoding = "utf-16") as f:
                for line in f:
                    count += 1.

            ClusterFile = io.open(filename, 'r', encoding = "utf-16")

        except:
            count = 0 
            with open(filename, 'r') as f:
                for line in f:
                    count += 1.

            ClusterFile = io.open(filename, 'r')

        list_clus_belong_photos = []

        for i in range(0, int(count)):

            line = ClusterFile.readline()
    
            list_line = line.split('\t')                  
            photo_id = list_line[0]             
            cluster_number = list_line[1]
            def_list = [photo_id,cluster_number]
            list_clus_belong_photos.append(def_list)
            
        ClusterFile.close()

        return(list_clus_belong_photos)

    def RunHtml(self): 

        new = 2
        # url = 'http://localhost:8000/Desktop/TFG/Code_Python/d3/index.html'
        url = 'http://127.0.0.1:64688/index.html'
        webbrowser.open(url,new=new)

        return

    def Exit(self):
        exit()
        return   
  
##-- End of Class 1: Win1 --##

# ------------------------------------------

# Class 2: Win2 
class Win2():

    def __init__(self, master, num_topic,editable_names,folder_topic,order_clusters):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        Color_List = ['silver','rosybrown', 'lightcoral','navy', 'maroon', 'red', 'tomato','sienna','peru','darkorange',
                        'gold', 'olive', 'yellow','purple', 'yellowgreen', 'darkolivegreen','deeppink', 'lawngreen', 'lightgreen',
                        'mediumaquamarine', 'turquoise', 'paleturquoise', 'darkcyan','aqua','deepskyblue', 'steelblue', 
                        'dodgerblue', 'blueviolet','magenta', 'mediumvioletred',  'hotpink', 'crimson', 'pink']

        name_topic = self.FrameUP(num_topic,Color_List)

        list_similarity = self.ReadRGTFile(num_topic,name_topic)
        
        list_clus_belong_photos = self.ReadDGTFile(num_topic,name_topic)

        if(order_clusters == 0):
            aux = 0
            list_images_url = self.Reading_folder_images(num_topic,folder_topic)
            list_images_resized =  self.ResizePhotos(list_images_url,aux)

        if(order_clusters == 1):
            aux = 1
            list_images_url = self.MakeURLDGT(list_clus_belong_photos,name_topic)
            list_images_resized =  self.ResizePhotos(list_images_url,aux)        

        self.FramesDown(list_images_url,num_topic,name_topic,Color_List,editable_names,list_images_resized,order_clusters,list_similarity,list_clus_belong_photos)
        
        return

    def FrameUP(self,num_topic,Color_List):
        
        name_topic = self.Read_topics_file(num_topic)
        Label_Topic = Label(self.frame, text = "TOPIC "+ num_topic +": "+ name_topic)

        Button_Legend = Button(self.frame, text="Legend",command= lambda: self.LegendFrame(num_topic,name_topic,Color_List))

        label_empty_1 = Label(self.frame, text="   ")
        label_empty_2 = Label(self.frame, text="   ")
        label_empty_3 = Label(self.frame, text="   ")

        Label_Topic.grid(row=0, column= 2)
        Button_Legend.grid(row=0, column = 4)
        label_empty_1.grid(row=0, column= 0)
        label_empty_2.grid(row=0, column= 1)
        label_empty_3.grid(row=0, column= 3)

        return (name_topic)

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

    def LegendFrame(self, num_topic,name_topic,Color_List):

        self.new = Toplevel(self.frame)        
        self.new.geometry("640x640")
        self.new.title("Legend Window")
        
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

    def ReadDclusterGT(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dclusterGt.txt"
        else:
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

    def ReadRGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/rGT/" + name_topic + " rGt.txt"
        else:
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

        rGT_file.close()

        return (list_similarity)

    def ReadDGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dGt.txt"
        else:
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

    def Reading_folder_images(self,num_topic,folder_topic):

        self.a = "a\ "
        self.b = self.a[1]
        self.image_list = []
        self.image_url = []

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

    def listToString(self,s):
         
        str1 = ""
  
        for ele in s:  
            str1 += ele   
          
        return str1

    def ResizePhotos(self,list_url_images,order_clusters):

        list_photo_type = []
        img_type = 0
        size_original_list = len(list_url_images)
            
        for i in range(0, size_original_list):

            img = Image.open(list_url_images[i])

            width,height = img.size

            if(width > height):
                prop = width / 300
                height_prop = int(height / prop)
                img = img.resize((300,height_prop), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 1
                pack = [img_def,img_type]

            if(width < height):
                prop = height / 300
                width_prop = int(width / prop)
                img = img.resize((185,300), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 2
                pack = [img_def,img_type]

            if(width == height):
                img = img.resize((300,300), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 3
                pack = [img_def,img_type]

            list_photo_type.append(pack)

        return list_photo_type

    def MakeURLDGT(self,list_clus_belong_photos,name_topic):

        size_list = len(list_clus_belong_photos)
        
        list_dgt_url_images = []

        for i in range(0,size_list):

            _pack = list_clus_belong_photos[i]
            id_photo_dgt = _pack[0]
            image_path = URL_IMAGES + name_topic + "/" + id_photo_dgt + ".jpg"

            list_dgt_url_images.append(image_path)

        return(list_dgt_url_images)

    def FramesDown(self,images_vector,num_topic, name_topic,Color_List,editable_names,images_vector_jpg,order_clusters,list_similarity,list_clus_belong_photos):
        
        frame_canvas = Frame(self.frame)
        frame_canvas.grid(row=1, column=0, columnspan=5, sticky='nw')
       
        GENERAL_CANVAS = Canvas(frame_canvas,width=1510, height=750, bg='white')
        GENERAL_CANVAS.grid(row=0, column=0)

        scrollbar = Scrollbar(frame_canvas,orient="vertical",command=GENERAL_CANVAS.yview)       
        scrollbar.grid(row=0, column=1, sticky='ns')

        GENERAL_CANVAS.configure(yscrollcommand=scrollbar.set)

        frame_fotos = tk.Frame(GENERAL_CANVAS)
        GENERAL_CANVAS.create_window((0,0), window=frame_fotos, anchor='nw')
        
        _num_fotos = 0
        self.images_vector_jpg = images_vector_jpg
        fotos_num = len(self.images_vector_jpg)

        if(order_clusters == 1):

            columns = 6

            if(fotos_num % 5 == 0):
                rows = int(fotos_num / 5) + 1
            else:
                rows = int(fotos_num / 5) + 2
            
        else:

            number_of_1 = 0
            number_of_0 = 0
            rows = 61
            columns = 6

        images_vector_url = images_vector
        frames_grid = [[Frame() for j in range(columns)] for i in range(rows)]
        canvas_grid = [[Canvas() for j in range(columns)] for i in range(rows)]

        for i in range (1, rows):

            _num_fotos += 1

            for j in range (1, columns):

                frames_grid[i][j] = Frame(frame_fotos)
                frames_grid[i][j].config(width=300,height=300)
                frames_grid[i][j].grid(row=i, column=j, sticky='n')

                if(_num_fotos <= fotos_num):

                    url_image = self.ExtractPhoto_fromUrl(images_vector_url[_num_fotos - 1])

                    canvas_grid[i][j] = Canvas(frames_grid[i][j], width=300, height=300)
                    canvas_grid[i][j].grid(row=0, column=0, columnspan=3)

                    self.pack = self.images_vector_jpg[_num_fotos-1]
                    self.img_type = self.pack[1]
                    self.image = self.pack[0]


                    if(self.img_type == 1):
                            
                        canvas_grid[i][j].create_image(0,40, image=self.image, anchor='nw')

                    if(self.img_type == 2):
                        
                        canvas_grid[i][j].create_image(55,0, image=self.image, anchor='nw')

                    if(self.img_type == 3):
                        
                        canvas_grid[i][j].create_image(0,0, image=self.image, anchor='nw')

                    _lbl_number = tk.Label(frames_grid[i][j], text="IMAGE "+str(_num_fotos))    
                    _lbl_number.grid(row=1, column=0, sticky='s')

                    if(editable_names == 1):

                        _photo_name = tk.Text(frames_grid[i][j], width=15, height=5)
                        _photo_name.grid(row=1, column=1, sticky='w')
                        _photo_name.insert(tk.END,url_image)

                    else:

                        _photo_name = Label(frames_grid[i][j], text=url_image)
                        _photo_name.grid(row=1, column=1, sticky='w')

                    _lbl_cluster = tk.Label(frames_grid[i][j])
                    _lbl_cluster.grid(row=1, column=2, sticky='w')

                    if(order_clusters == 0):
                        sim = self.SearchSimilarity(url_image,list_similarity)
                        aux = False
                    else:
                        sim = 1
                        aux = True

                    if(sim == 0):

                        number_of_0 += 1

                        canvas_grid[i][j].config(bg='white')            
                            
                        bckgrnd_lbl = 'red'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        _lbl_cluster.config(text="No Cluster", bg='black', fg='white')

                    elif(sim == 1):
                        
                        if(not aux):
                            number_of_1 += 1

                        color_bckgrn,number_cluster = self.SetColorCluster(url_image,list_clus_belong_photos,Color_List)
                        canvas_grid[i][j].config(bg=color_bckgrn)

                        bckgrnd_lbl = 'green'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        _lbl_cluster.config( text="Cluster "+str(number_cluster), bg=color_bckgrn)

                    else:
                        canvas_grid[i][j].config(bg='black')

                        bckgrnd_lbl = 'white'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        _lbl_cluster.config( text="No SIM", bg='white')

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
        
        btt_grapics_clusters = Button(self.frame, text="Pie Chart Clusters", command = lambda: self.PieChartGraphicCluster(name_topic,num_topic,list_clus_belong_photos,Color_List))
        btt_grapics_clusters.grid(row=2,column=2)

        if(order_clusters == 0):
            btt_graphics_similarity = Button(self.frame, text="Pie Chart Similarity", command = lambda: self.PieChartGraphicSimilarity(number_of_1,number_of_0))
            btt_graphics_similarity.grid(row=2,column=1)
        
        btt_close = Button(self.frame, text="Close", command = lambda: self.CloseWindow(images_vector_jpg,self.images_vector_jpg))
        btt_close.grid(row=2,column=3)

        return

    def ExtractPhoto_fromUrl(self,url):

        url_list = url.split('/')
        img_with_jpg = url_list[-1]
        aux = img_with_jpg.split('.')
        img_ = aux[0]

        return (img_)

    def SearchSimilarity(self, url_image,list_similarity):

        search = False
        list_length = len(list_similarity)
        number_of_0 = 0
        number_of_1 = 0
        counter = 0

        while((counter < list_length) and (not search)):

            _pack = list_similarity[counter]
            _photo_id = _pack[0]

            if(url_image == _photo_id):
                search = True
                if(int(_pack[1]) == 1):
                    sim = 1
                    
                elif(int(_pack[1]) == 0):
                    sim = 0
                
                else:
                    sim = -1     

            counter += 1

        return (sim)

    def SetColorCluster(self,url_image,list_clus_belong_photos,Color_List):

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

            try:         
                color = Color_List[int(number_cluster) - 1]
            except:
                color = Color_List[0]

        return(color,number_cluster)

    def PieChartGraphicCluster(self,name_topic,num_topic,list_clus_belong_photos,Color_List):

        list_clust = self.ReadDclusterGT(num_topic,name_topic)
        num_clust = len(list_clust)

        list_n_times = []
        colors = []

        length = len(list_clus_belong_photos)
        clusters_numbers = [int(i[1]) for i in list_clus_belong_photos]
        
        for i in range(0,num_clust):
            n_times = clusters_numbers.count(i+1)
            colors.append(Color_List[i])
            list_n_times.append(n_times)

        _labels = []
        _sizes = list_n_times

        for j in range(0, len(list_clust)):
            _labels.append('Topic '+str(j+1)+ ": " +list_clust[j] +"(" +str(list_n_times[j])+")")

        plt.figure(1)
        plt.pie(_sizes,  labels=_labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)

        plt.axis('equal')
        plt.show()
        
        return

    def PieChartGraphicSimilarity(self,number_of_1,number_of_0):
        
        sizes = [number_of_1, number_of_0]
        labels = ['Similarity (' + str(number_of_1) + ')', 'No Similarity (' + str(number_of_0) + ')']
        colors = ['green', 'red']
        explode = (0, 0)

        plt.figure(2)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)

        plt.axis('equal')
        plt.show()

        return

    def CloseWindow(self,images1,images2):

        del images1
        del images2

        self.master.destroy()

        return

##-- End of Class 2: Win2 --##

# ------------------------------------------

# Class 5: Win5
class Win5():

    def __init__(self, master,filename,path_filename):

        self.master = master
        self.frame = tk.Frame(self.master)

        result_list = self.ReadEvalFile(path_filename)

        num_topic,name_topic = self.Top_Frame(filename)
        self.Bottom_Frame(result_list,num_topic,name_topic)

        return

    def ReadEvalFile(self,path_filename):
        
        file_eval = open(path_filename, 'r')
  
        count = 0
        with open(path_filename, 'r') as f:
            for line in f:
                count += 1.

        list_result_eval = []

        for i in range(0, int(count)):

            line = file_eval.readline()
            list_line = line.split(' ')
            number_topic = list_line[0]
            id_photo = list_line[2]
            sim_photo = list_line[4]
            def_list = [number_topic,id_photo,sim_photo]
            list_result_eval.append(def_list)

        file_eval.close()

        return list_result_eval

    def Top_Frame(self,filename):

        num_topic = self.Extract_Number_of_filename(filename)

        name_topic = self.NameTopic(num_topic)

        lbl_filename = Label(self.master, text="FILE SELECTED: " + filename)
        lbl_filename.grid(row=0,column=1)

        lbl_topic_info = Label(self.master, text="Topic "+num_topic + ": "+ name_topic )
        lbl_topic_info.grid(row=0,column=3)
        
        return(num_topic,name_topic)

    def Extract_Number_of_filename(self, filename):

        units = filename[-5]

        try:
            tens = filename[-6]
            int_tens = int(tens)
            num_topic = tens + units
            aux_1_number = False
        except:
            ten_topics = ''
            num_topic = units
            aux_1_number = True

        try:
            hundreds = filename[-7]
            int_hundreds = int(hundreds)
            num_topic = hundreds + tens + units
        except:
            hundred = ''
            if(aux_1_number):
                num_topic =  units
            else:
                num_topic = tens + units

        return(num_topic)

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

    def Bottom_Frame(self,result_list,num_topic,name_topic):
        
        list_rgt = self.ReadRGTFile(num_topic,name_topic)

        list_dgt = self.ReadDGTFile(num_topic,name_topic)
        
        list_50_images = self.Make50ImagesList(result_list,name_topic)

        list_resized_photos =  self.ResizePhotos(list_50_images)

        list_sim_50_photos,number_of_ones,AP_list = self.Make50similarityList(list_rgt,result_list)

        num_of_clusters = self.ReadDclusterGT(num_topic,name_topic)
        
        list_clust_50 = self.Make50ClusterList(list_dgt,result_list)
        
        list_n_times_clust = self.MakeList_Compute_ClusterR(list_clust_50)
        
        self.MakeBotFrame(num_topic, name_topic,list_resized_photos,list_sim_50_photos,number_of_ones,AP_list,num_of_clusters,list_n_times_clust)

        return

    def ReadRGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/rGT/" + name_topic + " rGt.txt"
        else:
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

    def ReadDGTFile(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dGt.txt"
        else:
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

    def ResizePhotos(self,url_vector):

        list_photo_type = []
        img_type = 0

        for i in range(0, len(url_vector)):

            img = Image.open(url_vector[i])

            width,height = img.size

            if(width > height):
                prop = width / 300
                height_prop = int(height / prop)
                img = img.resize((300,height_prop), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 1
                pack = [img_def,img_type]

            if(width < height):
                prop = height / 300
                width_prop = int(width / prop)
                img = img.resize((185,300), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 2
                pack = [img_def,img_type]

            if(width == height):
                img = img.resize((300,300), Image.ANTIALIAS)
                img_def = ImageTk.PhotoImage(img)
                img_type = 3
                pack = [img_def,img_type]

            list_photo_type.append(pack)

        return list_photo_type

    def Make50similarityList(self,list_rgt,result_list):

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
            img_ex_file = pack_0[1]
            count_2 = 0
            search = False

            while( (count_2 < size_list_solutions) and (not search)):

                pack_ = list_rgt[count_2]
                img_sol_file = pack_[0]
                
                if(img_ex_file == img_sol_file):
                    
                    search = True
                    sim = int(pack_[1])             

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

    def ReadDclusterGT(self,num_topic,name_topic):

        if(int(num_topic) <= 70):
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/dGT/" + name_topic + " dclusterGt.txt"
        else:
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

    def Make50ClusterList(self,list_dgt,result_list):

        list_50_clust = []
        search = False
        size_list_examinations = len(result_list)
        
        size_list_solutions = len(list_dgt)
        count_1 = 0
        count_2 = 0

        while(count_1 < size_list_examinations):  

            pack_0 = result_list[count_1]
            img_ex_file = pack_0[1]
            count_2 = 0
            search = False   

            while( (count_2 < size_list_solutions) and (not search)):

                pack_ = list_dgt[count_2]
                img_sol_file = pack_[0]
                
                if(img_ex_file == img_sol_file):

                    search = True
                    clust = (pack_[1])
                    list_50_clust.append(clust)
             
                count_2 += 1

            count_1 += 1

        return(list_50_clust)
    
    def MakeList_Compute_ClusterR(self,list_clust_50):

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

    def MakeBotFrame(self,num_topic, name_topic,list_resized_photos,list_sim_50_photos,number_of_ones,AP_list,num_of_clusters,list_n_times_clust):

        precission_list = []
        Clust_Recall_list = []
        Cust_recall_graphic_list = []
        F1_score_list = []
        cont_aux = 0
        
        frame_canvas = Frame(self.master)
        frame_canvas.grid(row=1, column=0, columnspan=5, sticky='nw')
       
        GENERAL_CANVAS = Canvas(frame_canvas,width=1510, height=750, bg='white')
        GENERAL_CANVAS.grid(row=0, column=0)

        scrollbar = Scrollbar(frame_canvas,orient="vertical",command=GENERAL_CANVAS.yview)       
        scrollbar.grid(row=0, column=1, sticky='ns')

        GENERAL_CANVAS.configure(yscrollcommand=scrollbar.set)

        frame_fotos = tk.Frame(GENERAL_CANVAS)
        GENERAL_CANVAS.create_window((0,0), window=frame_fotos, anchor='nw')
        
        rows = 11
        columns = 6

        frames_grid = [[Frame() for j in range(columns)] for i in range(rows)]
        canvas_grid = [[Canvas() for j in range(columns)] for i in range(rows)]

        _num_fotos = 0
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

                    else:
                        bg_color='red'
                        if(len(Clust_Recall_list) == 0):
                            CR = 0
                            F1 = 0
                        else:
                            
                            CR = Clust_Recall_list[-1]
                            F1 = 2*((precision * CR)/(precision + CR))

                        cont_aux -= 1

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
                    self.img_type = self.pack[1]
                    self.image = self.pack[0]


                    if(self.img_type == 1):
                            
                        canvas_grid[i][j].create_image(0,40, image=self.image, anchor='nw')

                    if(self.img_type == 2):
                        
                        canvas_grid[i][j].create_image(55,0, image=self.image, anchor='nw')

                    if(self.img_type == 3):
                        
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
        btt_graphics.grid(row=2,column=1)

        btt_pie_chart = Button(self.master, text="Pie Chart Similarity", command= lambda: self.MakePieChart(precission_list,number_of_ones))
        btt_pie_chart.grid(row=2,column=2)

        btt_close_window = Button(self.master, text="Close", command= lambda : self.CloseWindow(list_resized_photos,self.images_vector_jpg))
        btt_close_window.grid(row=2,column=3)

        #End loop For------------------

        frame_fotos.update_idletasks()        
          
        GENERAL_CANVAS.config(scrollregion=GENERAL_CANVAS.bbox("all"))

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

    def MakeGraphics(self,precission_list,Cust_recall_graphic_list,F1_score_list):

        X_axis_list = list(range(0,len(precission_list)))

        fig, ax = plt.subplots()
        ax.plot(X_axis_list, precission_list, 'k',color='red', label='Precission')
        ax.plot(X_axis_list, Cust_recall_graphic_list, 'k',color='blue', label='Cluster Recall')
        ax.plot(X_axis_list, F1_score_list, 'k', color='green', label='F1 Score')

        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                fancybox=True, shadow=True, ncol=5)

        plt.show()


        return

    def MakePieChart(self,precission_list,number_of_ones):
        
        num_0 = len(precission_list) - number_of_ones
        sizes = [number_of_ones, num_0]
        colors = ['green', 'red']
        explode = (0, 0)
        labels = 'Similarity ('+ str(number_of_ones) + ')', 'No Similarity ('+ str(num_0) +')' 

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)

        plt.axis('equal')
        plt.show()

        return

    def CloseWindow(self,images1,images2):

        del images1
        del images2

        self.master.destroy()

        return

##-- End of Class 5: Win5 --##

# ------------------------------------------
root.title("Mediaeval2016 Image Tool")
root.geometry("%dx%d+%d+%d" % (width_window,height_window,coordinate_x,coordinate_y))

app = Win1(root)
app.mainloop()