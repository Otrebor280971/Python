def orden(a,b,c):
    if a < b and b < c:
        return "ASCENDENTE"
    elif a > b and b > c:
        return "DESCENDENTE"
    else:
        return "NO ORDENADO"

a = int(input())
b = int(input())
c = int(input())

respuesta = orden(a,b,c)

print(respuesta)