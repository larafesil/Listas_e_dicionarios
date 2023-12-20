from random import randint
lista = []
lista_recebe = []
print('-'*40)
print('           JOGO DA MEGA SENA       ')
print('-'*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= jogos:
    cont = 0
    while True:
        numeros = randint(1,60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista_recebe.append(lista[:])
    lista.clear()
    total += 1
print('-='*5, F' SORTEANDO {jogos} JOGOS ', '-='*5)
for i,l in enumerate(lista_recebe):
    print(f'Jogo {i+1}: {l}')

