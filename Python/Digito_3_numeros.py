numero = int(input("Ingresa el numero de 3 digitos:"))

centenas = numero//100
decenas = (numero-(centenas*100))//10
unidades = numero % 10
print(unidades,"unidades")
print(decenas,"decenas")
print(centenas,"centenas")