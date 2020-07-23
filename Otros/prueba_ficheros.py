##### PRUEBA LECTURA FICHEROS

f = open("C:/Users/Pedro/Desktop/TFG/prueba.txt", "r")
# line1 = f.readline()
# line2 = f.readline()

# print(line1)
# print(line2)
x = f.readline()
for x in f:
    
    y = f.readline()
    print(x)
    print(y)
    

# print(palabro[1])
f.close()