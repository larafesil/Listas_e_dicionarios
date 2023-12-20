from random import randint
from time import sleep
print('´-.' * 5, 'PEDRA, PAPEL E TESOURA', '´-.' * 5)
lista = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogada = int(input('Qual sua jogada? '))
print('´-.' * 20)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('´-.' * 20)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogada]))
if computador == 0: # PEDRA
    if jogada == 0: # PEDRA
        print('EMPATE')
    elif jogada == 1: # PAPEL
        print('JOGADOR VENCE')
    elif jogada == 2: # TESOURA
        print('COMPUTADOR VENCE')
elif computador == 1: # PAPEL
    if jogada == 0: # PEDRA
        print('COMPUTADOR VENCE')
    elif jogada == 1: # PAPEL
        print('EMPATE')
    elif jogada == 2: # TESOURA
        print('JOGADOR VENCE')
elif computador == 2: # TESOURA
    if jogada == 0: # PEDRA
        print('JOGADOR VENCE')
    elif jogada == 1: # PAPEL
        print('COMPUTADOR VENCE')
    elif jogada == 2: # TESOURA
        print('EMPATE')


