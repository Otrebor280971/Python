texto = "Hola, buen día"
cifrado = ""

for t in range(len(texto)):
    codigo = (ord(texto[t]) + (t+1))
    NL = chr(codigo)
    cifrado += NL

print(texto)
print(cifrado)
