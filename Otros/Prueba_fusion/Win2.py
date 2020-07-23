def __init__(self, master, num_topic,editable_names,folder_topic,order_clusters):

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

        name_topic = self.FrameUP(num_topic,Color_List)

        #Read rGT file
        list_similarity = self.ReadRGTFile(num_topic,name_topic)
        

        #Read dGT file
        list_clus_belong_photos = self.ReadDGTFile(num_topic,name_topic)


        if(order_clusters == 0):
            list_images_url = self.Reading_folder_images(num_topic,folder_topic)
            list_images_resized =  self.ResizePhotos(list_images_url)


        if(order_clusters == 1):
            list_images_url = self.MakeURLDGT(list_clus_belong_photos,name_topic)
            list_images_resized =  self.ResizePhotos(list_images_url)
        
        self.FramesDown(list_images_url,num_topic,name_topic,Color_List,editable_names,list_images_resized,order_clusters,list_similarity,list_clus_belong_photos)
    

        return



def FramesDown(self,images_vector,num_topic, name_topic,Color_List,editable_names,images_vector_jpg,order_clusters,list_similarity,list_clus_belong_photos):
        
        
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
        
       
        
        _num_fotos = 0#contador para las fotos
        fotos_num = len(images_vector) #cuantos elementos hay en el vector
        self.images_vector_jpg = images_vector_jpg

        if(order_clusters == 1):
            columns = 6
            rows = fotos_num % 5 + int(fotos_num / 5) + 1
        else:

            number_of_1 = 0
            number_of_0 = 0
            rows = 61
            columns = 6


        frames_grid = [[Frame() for j in range(columns)] for i in range(rows)]
        canvas_grid = [[Canvas() for j in range(columns)] for i in range(rows)]


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

                    
                    if(order_clusters == 0):
                        sim = self.SearchSimilarity(url_image,list_similarity)
                    else:
                        sim = 1
                        aux = True


                    if(sim == 0):

                        number_of_0 += 1

                        canvas_grid[i][j].config(bg='white')            
                            
                        bckgrnd_lbl = 'red'
                        _lbl_number.config(bg=bckgrnd_lbl)

                        _lbl_cluster.config(text="No Cluster", bg='black', fg='white')

                    else:
                        
                        if(not aux):
                            number_of_1 += 1

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
        
        btt_grapics_clusters = Button(self.frame, text="Pie Chart Clusters", command = lambda: self.PieChartGraphicCluster(name_topic,num_topic,list_clus_belong_photos,Color_List))
        btt_grapics_clusters.grid(row=2,column=2)

        if(order_clusters == 0):
            btt_graphics_similarity = Button(self.frame, text="Pie Chart Similarity", command = lambda: self.PieChartGraphicSimilarity(number_of_1,number_of_0))
            btt_graphics_similarity.grid(row=2,column=1)

        return