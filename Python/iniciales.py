nombre = input("Nombre: ")
print(nombre)

iniciales = nombre.split (" ")
for i in range(len(iniciales)):
    print(iniciales[i][0], end = "")