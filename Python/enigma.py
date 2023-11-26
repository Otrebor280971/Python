mensaje = str(input())
H = str("H")
diferencia = ord(mensaje[-1]) - ord(H[0])
i = 0
mensaje_desif = str("")

while i < len(mensaje):
    nueva = chr(ord(mensaje[i])-diferencia)
    mensaje_desif += nueva
    i = i+1
    
    
print(diferencia)
print(mensaje_desif)