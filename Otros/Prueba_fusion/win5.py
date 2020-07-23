def __init__(self, master,filename,path_filename):

        self.master = master
        self.frame = tk.Frame(self.master)

        # Leer el fichero
        # mostrar  fotos (basarse en la clase 2)
        result_list = self.ReadEvalFile(path_filename)

        num_topic,name_topic = self.Top_Frame(filename)
        self.Bottom_Frame(result_list,num_topic,name_topic)

        

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

   
	#End loop For------------------

	
	frame_fotos.update_idletasks()        
	  
	GENERAL_CANVAS.config(scrollregion=GENERAL_CANVAS.bbox("all"))

	return