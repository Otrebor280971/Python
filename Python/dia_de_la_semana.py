def dia_habil(dia,mes,ano):
    a = (14- mes) // 12
    y = ano - a
    m = mes +12 * a-2
    d = (dia + y + y // 4 - y //100 + y //400 + 31*m//12)%7
    
    if d == 0 or d == 6:
        return "FIN DE SEMANA"
    else: 
        return "DIA HABIL"
    
dia = int(input())
mes = int(input())
ano = int(input())

respuesta = dia_habil(dia,mes,ano)

print(respuesta)