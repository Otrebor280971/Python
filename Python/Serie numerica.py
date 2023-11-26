print("Calculemos la serie numerica")
num1 = int(input("Dime el primer número de la serie:"))
num2 = int(input("Dime el siguiente número:"))
num3 = int(input("Dime el tercer número:"))

#Continuación serie 
num4 = (num2 - num1) + num3
num5 = (num3-num2)+ num4
print("La serie es " + str(num1) + "," + str(num2) + "," + str(num3) + "," + str(num4) + "," + str(num5))