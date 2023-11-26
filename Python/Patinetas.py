print("Calculemos cuantas patinetas se pueden hacer")

tablas = int(input("Ingresa la cantidad de tablas en inventario:"))
ruedas = int(input("Ingresa la cantidad de ruedas en inventario:"))

#No de tablas posibles
notablas = tablas/2
#No de rueds posibles
noruedas = ruedas/4
#No de patinetas fabricables
patinetas = min(notablas,noruedas)

print("Se pueden realizar " + str(int(patinetas)) + " patinetas con los materiales del inventario")