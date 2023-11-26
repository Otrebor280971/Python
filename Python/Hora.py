#Programa 1
hora = int(input("Ingresa la hora en formato 24 hrs:"))
minutos = int(input("Ingresa los minutos:"))
segundos = int(input("Ingresa los segundos:"))

segundos = segundos + 1
if segundos == 60:
    minutos = minutos + 1
    segundos = 0

if minutos == 60:
    hora = hora + 1
    minutos = 0

print(str(hora) + ":" + str(minutos) + ":" + str(segundos))
print("Fin programa 1")


#Programa 2
horas = int(input("Ingresa la hora:"))
minuto = int(input("Ingresa los minutos:"))
segundo = int(input("Ingresa los segundos:"))

segundo = segundo + 1
if segundo >= 60 and minuto <=58:
    minuto = minuto + 1
    segundo = 0
    print(str(horas) + ":" + str(minuto) + ":" + str(segundo))
elif segundo >= 60 and minuto >=59:
    horas = horas + 1
    segundo = 0
    minuto = 0
    print(str(horas) + ":" + str(minuto) + ":" + str(segundo))
else :
    print(str(horas) + ":" + str(minuto) + ":" + str(segundo))


print("Fin programa 2")

#El programa 1 es la mejor solución ya que simplifica las evaluaciones de los datos