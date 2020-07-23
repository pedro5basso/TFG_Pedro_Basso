import io
import shutil

PATH_TO_SAVE = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files'
FILE_TO_MODIFY = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/hola.txt'

num_topic = '79'
name_topic = 'blanket_on_sofa'


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
    def_list = photo_id+','+cluster_number
    list_clus_belong_photos.append(def_list)

# oline=dGT_file.readlines()
dGT_file.close()



with open(FILE_TO_MODIFY, 'w') as f:
    for item in list_clus_belong_photos:
        f.write("%s" % item)


src=open(FILE_TO_MODIFY,"r")
fline="PRIMERA LINEA\n"    #Prepending string
oline=src.readlines()
#Here, we prepend the string we want to on first line
oline.insert(0,fline)
src.close()
 
 
#We again open the file in WRITE mode 
src=open(FILE_TO_MODIFY,"w")
src.writelines(oline)
src.close()


