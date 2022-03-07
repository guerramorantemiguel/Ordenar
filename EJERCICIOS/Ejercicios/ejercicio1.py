import random

tabla = []
for i in range (len(tabla)):
    for j in range(len(tabla)):
        if tabla[i] > tabla[j]:
            aux = tabla[i]
            tabla[i] = tabla[j]
            tabla[j] = aux
print(tabla)


   