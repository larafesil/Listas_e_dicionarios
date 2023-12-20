valores = []
continuar = ''
while True:
    numero = int(input(f'Digite um número: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, tente novamente...')
    continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
print('=-'*30)
valores.sort()
print(f'Você adicionou {valores}')

