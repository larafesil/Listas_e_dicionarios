pessoas = list()
dados = list()
#maior_peso = list()
#menor_peso = list()
total_pessoas = maior = menor = 0
#continuar = ''
while True:
    dados.append(str(input('Nome: ')))
    dados.append((float(input('Peso: '))))
    total_pessoas += 1
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar?[S/N] => ').upper().strip()[0]
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
print(f'Foram cadastradas o total de {total_pessoas} pessoas.')
print(f'O maior peso foi de {maior:.2f}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor:.2f}KG.', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()


