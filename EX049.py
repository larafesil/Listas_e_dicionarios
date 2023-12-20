from time import sleep
print('============================ TABUADA ============================')
print('Seja bem vindo(a) a tabuada interativa, é muito fácil de usar:')
print('='* 65)
sleep(3)
print('='* 65)
print('''ORIENTAÇÕES:
1° PASSO: Digite o número que você quer ver a tabuada.
2º PASSO: Digite a opção que deseja fazer a operação.
Obs: Tabuada simplificada até o número 10. Se divirta!''')
print('='* 65)
sleep(3)
print('='* 65)
numero = float(input('Digite um número: '))
print('='* 65)
print('''Suas opções:
[ 1 ] ADIÇÃO
[ 2 ] SUBTRAÇÃO
[ 3 ] DIVISÃO
[ 4 ] MULTIPLICAÇÃO''')
print('='* 65)
opção = int(input('Digite sua opção: '))
print('='* 65)
print('GERANDO TABUADA... AGUARDE')
sleep(2)
for a in range(3,0,-1):
    print(a)
    sleep(1)
print('='* 65)
for c in range(1,11):
    if opção == 1:
        print('{:.0f} + {} = {:.0f}'.format
              (numero, c, numero + c))
    elif opção == 2:
        print('{:.0f} - {} = {:.0f}'.format
              (numero, c, numero - c))
    elif opção == 3:
        print('{:.0f} ÷ {} = {:.0f}'.format
              (numero, c, numero / c))
    elif opção == 4:
        print('{:.0f} x {} = {:.0f}'.format
              (numero, c, numero * c))
    else:
        print('Opção inválida, tente novamente')
