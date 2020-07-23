import glob
import io


def listToString(s):
         
        str1 = ""
  
        for ele in s:  
            str1 += ele   
          
        return str1

folder_topic = 'C:/Users/Pedro/Desktop/TFG/Dades 16/images/collection/blueberry_on_plant'

image_url = []

a = "a\ "
b = a[1]

for filename in glob.glob(folder_topic+"/*.jpg"):
    A = list(filename)
    
    i = 0
    
    for c in filename:
        if (c == b):
            A[i] = '/'
        
        i = i +1

    image_url_def = listToString(A)
    url_separated = image_url_def.split('/')
    name_photo_jpg = url_separated[-1]
    name_photo_ = name_photo_jpg.split('.')
    name_photo = name_photo_[0]
    image_url.append(name_photo)

num_topic = str(80)
filename = 'images_files/topic'+num_topic+'.txt'

try:

    f = open(filename,'x') 
    f.close()

    
    with open(filename, 'w') as f:
        for item in image_url:
            f.write("%s\n" % item)

    f.close()
    print('txt file generated correctly!')

except:

    print('the txt file as created before')
    f = open(filename,'r')

    first_line  = f.readline()
    print('primera linea: ', first_line)
    f.close()