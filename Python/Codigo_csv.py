import os

inFile = open('countries.csv','r')
content = inFile.read()

print(content)

lista = content.splitlines()
for i in range(len(lista)):
    lista[i] = lista[i].split(sep=',')

print(lista[0:5])

for pais in lista:
    print(pais)

inFile.close()