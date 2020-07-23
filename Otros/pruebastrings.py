# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1 

a = "\Hola"
b = a[0]
v = r"C:\Users\Pedro\Desktop\TFG\Imagenes_TFG\topic97\topic97162317526.jpg"
A = list(v)

i = 0
for c in v:
    if (c == b):
        A[i] = '/'
    
    i = i +1

print(listToString(A))