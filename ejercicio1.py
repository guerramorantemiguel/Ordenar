# Ordenación por inserción dicotómica
import random

tabla = []
def generartabla(i, n):
    j = i.split(" ")
    while len(tabla) < i:
        tabla.append(random.randint(int(j[0])), int(j[1]))

generartabla(int(input("Introduzca cuántos elementos desea que tenga su tabla: ")))