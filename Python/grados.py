#Programa 1
grados = int(input("Ingresa el valor entero en grados:"))

if grados < 0 or grados > 360 :
    print("El valor se encuentra fuera de rango")
elif grados == 0 or grados == 90 or grados == 180 or grados == 270 or grados == 360:
    print("El valor se encuentra en un eje")
elif grados >= 1 and grados <= 89:
    print("El valor se encuentra en el cuadrante 1")
elif grados >= 91 and grados <= 179:
    print("El valor se encuentra en el cuadrante 2")
elif grados >= 181 and grados <= 269:
    print("El valo se encuentra en el cuadrante 3")
elif grados >=271 and grados <= 359:
    print("El valor se encuentra en el cuadrante 4")

print ("Fin del programa 1")

#Programa 2
n = int(input("Valor entero en grados:"))

if n >=1 and n <= 89:
    print("Cuadrante 1")
elif n >= 91 and n <= 179:
    print("Cuadrante 2")
elif n >= 181 and n <= 269:
    print("Cuadrante 3")
elif n >= 371 and n <= 359:
    print("Cuadrante 4")
elif n == 0 or n == 90 or n == 180 or n == 270:
    print("Sobre un eje")
else :
    print("Valor fuera de rango")

print("Fin programa 2")

#Ambos programas funcionan igual, solo que el programa 2 cuenta con el else para evitar hacer la evaluación en los valores fuera de rango