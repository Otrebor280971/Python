dia_persona1 = int(input())
dia_persona2 = int(input())

def compatibilidad(numero):
    while numero > 9:
        suma_digitos = 0
        while numero > 0:
            suma_digitos += numero % 10
            numero //= 10
        numero = suma_digitos
    return numero

def verificar_compatibilidad(persona1, persona2):
    factor_persona1 = compatibilidad(persona1)
    factor_persona2 = compatibilidad(persona2)
    
    if factor_persona1 % 2 == 0 and factor_persona2 % 2 == 0:
        return "SI"
    else:
        return "NO"
resultado = verificar_compatibilidad(dia_persona1, dia_persona2)
print(resultado)