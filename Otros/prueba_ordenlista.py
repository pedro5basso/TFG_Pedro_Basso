
list_clust_50 = [1,4,5,6,4,4,4,5]
# def_list = []
# aux_list = []
# cont = 1
# def_list.append(cont)

# search = False


# muestra_inicial = list_clust_50[0]

# if(muestra_inicial == 0):
#     muestra_inicial = list_clust_50[1]
#     i = 2
#     def_list.append(cont)

# else:
#     muestra_inicial = list_clust_50[0]
#     aux_list.append(list_clust_50[0])
#     i=1


# while( i < len(list_clust_50)):
    
#     aux_list.append(muestra_inicial)

#     if (list_clust_50[i] != 0):
#         if(aux_list.count(list_clust_50[i]) == 0):
#             cont +=1
            
#         muestra_inicial = list_clust_50[i]

#     def_list.append(cont)
#     i += 1
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

print(def_list)