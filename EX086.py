lista = [[], [], []]
valor = 0
pares = 0
maior = 0
for c in range(0,3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    lista[0].append(valor)
    if valor % 2 == 0:
        pares += valor
for c in range(0,3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    lista[1].append(valor)
    if valor % 2 == 0:
        pares += valor
for c in range(0,3):
    valor = int(input(f'Digite um valor para [2, {c}]: '))
    lista[2].append(valor)
    if valor % 2 == 0:
        pares += valor
print('-='*17)
print(f'[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]')
print(f'[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]')
print(f'[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]')
print('-='*17)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {lista[0][2]+lista[1][2]+lista[2][2]}')
for n in lista[1]:
    if n == 0:
        maior = n
    else:
        if n > maior:
            maior = n
print(f'O maior valor da segunda linha é {maior}.')