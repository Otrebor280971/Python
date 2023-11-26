num_alumnos = int(input())

total_calificaciones = 0
calificacion_mas_alta = 0
calificacion_mas_baja = 100

alumnos = 0

while alumnos < num_alumnos:
    calificacion = int(input())
    total_calificaciones += calificacion
    if calificacion > calificacion_mas_alta:
        calificacion_mas_alta = calificacion
    if calificacion < calificacion_mas_baja:
        calificacion_mas_baja = calificacion
    alumnos += 1
promedio = total_calificaciones / num_alumnos

print(promedio)
print(calificacion_mas_alta)
print(calificacion_mas_baja)