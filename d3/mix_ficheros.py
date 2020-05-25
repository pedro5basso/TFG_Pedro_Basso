

num_topic = '77'
name_topic = 'birthday_candle'



# fichero RGT
def ReadRGTFile(num_topic,name_topic):


        if(int(num_topic) <= 70): #the file is in devset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/devset/rGT/" + name_topic + " rGt.txt"
        else:#the file is in testset folder
            filename = "C:/Users/Pedro/Desktop/TFG/b/gt/testset/rGT/" + name_topic + " rGt.txt"


        rGT_file = open(filename, 'r')

        list_similarity = []

        count = 0
        with open(filename, 'r') as f:
            for line in f:
                count += 1.

        for i in range(0, int(count)):

            line = rGT_file.readline()
            list_line = line.split(',')
            id_photo = list_line[0]
            sim_photo = list_line[-1]
            def_list = [id_photo,sim_photo]
            list_similarity.append(def_list)

        rGT_file.close()

        return (list_similarity)

# fichero dclusterGT
def ReadDclusterGT(num_topic,name_topic):

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

# fichero dGT
def ReadDGTFile(num_topic,name_topic):

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

# fichero Custers
def ReadClustersFile(num_topic,name_topic):


        file_path = 'C:/Users/Pedro/Desktop/TFG/soluciones/clusterings/'+num_topic+'-'+name_topic+'-Clusters.txt'

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


filerGT = ReadRGTFile(num_topic,name_topic)
filedGT = ReadDGTFile(num_topic,name_topic)
filedclusterGT = ReadDclusterGT(num_topic,name_topic)
fileClusters = ReadClustersFile(num_topic,name_topic)


# Formato del fichero
# ID_PHOTO,SIMILARITY,ID_CLUSTER,NAME_CLUSTER
# 