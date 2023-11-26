ancho = int(input("Ancho de pesa:"))
espacios = ancho//2 - 1
huecos = ancho%2

print(ancho * "-")
print(ancho * "-")
print(espacios*" " + "!" + huecos*" " + "!")
print(ancho * "-")
print(ancho * "-")