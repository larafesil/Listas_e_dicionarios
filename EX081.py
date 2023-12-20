contador = 0
continuar = ''
lista = []
while True:
    n = int(input('Digite um valor: '))
    contador += 1
    lista.append(n)
    continuar = input('Você quer continuar? [S/N] ').strip()[0].upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print(f'Você adicionou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não está inserido na lista')
print('PROGRAMA ENCERRADO, ATÉ A PRÓXIMA')
