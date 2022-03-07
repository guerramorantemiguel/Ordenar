# Ordenación por inserción dicotómica
import random

tabla = []
def generartabla(n, i):
    j = i.split(" ")
    while len(tabla) < n:
        tabla.append(random.randint(int(j[0])), int(j[1]))

generartabla(int(input("Introduzca cuántos elementos desea que tenga su tabla en un rango 1-50: ")))
print("Su tabla inicial es la siguiente: " + str(tabla))
