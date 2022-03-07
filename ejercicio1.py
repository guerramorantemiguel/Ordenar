tabla = [5, 7, 3, 2, 10, 9]
for i in range (len(tabla)):
    for j in range(len(tabla)):
        if tabla[i] > tabla[j]:
            aux = tabla[i]
            tabla[i] = tabla[j]
            
   