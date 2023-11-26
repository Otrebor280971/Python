frase = input(".")
password = input(".")


cifr = ""

for i in range(len(frase)):
    cifr += chr(ord(frase[i]) + ord(password[i % len(password)]))

print(cifr)