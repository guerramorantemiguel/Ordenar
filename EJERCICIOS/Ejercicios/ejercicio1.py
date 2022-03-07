import random

tabla = []

def generartabla(n, i):
    j = i.split("-")
    tabla.append(random.randint(int(j[0]), int(j[1])))
    
for i in range (len(tabla)):
    for j in range(len(tabla)):
        if tabla[i] > tabla[j]:
            aux = tabla[i]
            tabla[i] = tabla[j]
            tabla[j] = aux
print(tabla)


   