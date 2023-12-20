from random import shuffle
print('ORDEM DE APRESENTAÇÃO')
print('')
a1 = input('Aluno: ')
a2 = input('Aluno: ')
a3 = input('Aluno: ')
a4 = input('Aluno: ')
lista = [a1,a2,a3,a4]
shuffle(lista)
print('a ordem de apresentação é a seguite:')
print(lista)