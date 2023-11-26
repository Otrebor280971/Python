opm = int(input("Oscilaciones por minuto:"))

if opm >=100:
    print("Alerta roja")
elif opm >=20:
    RK = opm/100
    print("Alerta Amarilla, RK= " + str(RK))
else:
    print("Normal")