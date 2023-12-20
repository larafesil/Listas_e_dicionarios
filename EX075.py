tupla = ()
tupla_par = ()
n1 = int(input('1º numero: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
n4 = int(input('4º número: '))
tupla = (n1,n2,n3,n4)
if n1 % 2 == 0:
    tupla_par = (n1)
if n2 % 2 == 0:
    tupla_par = (n2)
if n3 % 2 == 0:
    tupla_par = (n3)
if n4 % 2 == 0:
    tupla_par = (n4)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {tupla_par}')