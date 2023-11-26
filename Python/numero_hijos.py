import random

n = int(input("Numero de simulaciones:"))
sim = 1
suma = 0

while sim <=n:
    print("---Simulación", sim)
    niños = 0
    niñas = 0
    while niños == 0 or niñas == 0:

        bb = random.randint(0,1)
        if bb == 1:
            niños = niños + 1
            print("niño", end=" ")
        else:
            niñas = niñas + 1
            print("niña", end=" ")
        
    print("\nHijos:", niños + niñas)
    suma = suma + niños + niñas
    sim = sim + 1
prom = suma / n
print("Promedio de hijos:", int(prom))