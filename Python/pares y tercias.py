card_counts = {'Q': 0, 'J': 0, 'K': 0}

for _ in range(3):
    card = input()
    
    if card in card_counts:
        card_counts[card] += 1

pares = 0
tercias = 0

for count in card_counts.values():
    if count == 2:
        pares += 1
    elif count == 3:
        tercias += 1

print(pares)
print(tercias)
