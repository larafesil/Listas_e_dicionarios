lista_pares = []
lista_impares = []
lista = []
continuar = ''
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print(f'A lista completa é {lista}')
print(f'Os números pares digitados foram {lista_pares}')
print(f'Os números ímpares digitados foram {lista_impares}')
