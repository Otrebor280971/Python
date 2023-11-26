import shelve
import os

archivo = shelve.open('123')
llave = archivo.keys()

if "nombre" in llave:
    nombre = archivo["nombre"]
    print("Hola", nombre)
    notas = archivo["notas"]
    print(notas)
    nota = input("Nota:")
    notas.append(nota)
    archivo["notas"] = [notas]

else:
    nombre = input("Cual es tu nombre:")
    archivo["nombre"] = nombre
    nota = input("Nota:")
    archivo["notas"] = [nota]

archivo.close()