numero = int(input())
suma_divisores = 0
i = 1

while i < numero:
    if numero % i == 0:
        suma_divisores += i
    i += 1

if suma_divisores == numero:
    print("SI")
else:
    print("NO")
