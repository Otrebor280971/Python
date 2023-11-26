def descifrar_mensaje(cifrado):
    longitud_original = len(cifrado) % 2

    grupos = [cifrado[i:i+3] for i in range(0, len(cifrado), 3)]


    mensaje_descifrado = ""
    for grupo in grupos:

        codigo_numerico = int(grupo)


        if longitud_original % 2 == 0:
            codigo_numerico -= 1
        else:
            codigo_numerico += 1

        mensaje_descifrado += chr(codigo_numerico)

    return mensaje_descifrado

mensaje_cifrado = input()
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)
print(mensaje_descifrado)