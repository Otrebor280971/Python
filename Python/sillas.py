sil = int(input("Tipo de silla:"))
clnt = int(input("Tipo de cliente:"))
cant = int(input("Cantidad de sillas:"))

if sil ==1:
    sub = 700*cant
else:
    sub = 900*cant

if clnt == 1:
    if sub>10000:
        desc = sub*0.1
    else:
        desc = 0
else:
    desc = sub*0.2

ttl = sub-desc

print(float(sub))
print(float(desc))
print(float(ttl))