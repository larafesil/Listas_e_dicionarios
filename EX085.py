lista_pares_impares = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º número: ')))
    if valor % 2 == 0:
        lista_pares_impares[0].append(valor)
    if valor % 2 == 1:
        lista_pares_impares[1].append(valor)
lista_pares_impares[0].sort()
lista_pares_impares[1].sort()
print(f'Os valores pares digitados foram {lista_pares_impares[0]}')
print(f'Os valores ímpares digitados foram {lista_pares_impares[1]}')