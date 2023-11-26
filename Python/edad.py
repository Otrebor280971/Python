edad = 969

num = 0

while num < edad or num > edad:
    num = int(input("Indique una edad:"))
    if num < edad:
        print("La edad de Matusalen es mayor")
    elif num > edad:
        print("La edad de Matusalen es menor")

if num == edad:
    print("Respuesta correcta")    