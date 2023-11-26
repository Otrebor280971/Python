contador_ceros = 0
contador_unos = 0
print("Ingresa los 5 digitos binarios 1 por 1")
for binarios in range(5):
    digito = int(input("Ingresa un dígito binario (0 o 1): "))
    
    #Contador 1 y 0
    if digito == 0:
        contador_ceros += 1
    elif digito == 1:
        contador_unos += 1

print("Número de ceros: " + str(contador_ceros))
print("Número de unos: " + str(contador_unos))
