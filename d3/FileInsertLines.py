import shutil

#We read the existing text from file in READ mode
src=open("prueba.txt","r")
fline="line 98\n"    #Prepending string
oline=src.readlines()
#Here, we prepend the string we want to on first line
oline.insert(0,fline)
src.close()
 
 
#We again open the file in WRITE mode 
src=open("prueba.txt","w")
src.writelines(oline)
old_path = 'C:/Users/Pedro/Desktop/TFG/Code_Python/prueba.txt'
path_new = 'C:/Users/Pedro/Desktop/TFG/Code_Python/d3/files/hola.txt'
src.close()

shutil.copy(old_path, path_new)