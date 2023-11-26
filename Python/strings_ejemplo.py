string = "hola"
print(string)
print(len(string))
print(string[1])


#Si no existe, el .find() devuelve un -1
index = string.find("a")
print(index)

#Meter .replace() para que se cambie
texto = string.replace("hola", "HOLA")
print(texto)

letra = string[0]
codigo = ord(letra)
print(codigo)

num = 937
sim = chr(num)
print(sim)

dato = "1 27 3540 -454"
lista = dato.split(sep=" ")
print(lista)

print("\"a\nb\\")