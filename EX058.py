from random import randint
acertou = False
facil = randint(0,5)
medio = randint(0,10)
dificil = randint (0,15)
print('========= Bem vindo ao jogo da advinhação ==========')
print('''ESCOLHA A DIFICULDADE:
[ 1 ] FÁCIL
[ 2 ] INTERMEDIÁRIO
[ 3 ] DIFICIL''')
escolha = int(input('Digite o número correspondente ao nivel: '))
if escolha == 1:
    print('Você escolheu o nivel FÁCIL, vamos começar...')
    print('Estou pensando em um número entre 0 e 5, você consegue acertar??')
    while not acertou:
        jogador = int(input('Digite seu palpite: '))
        if jogador == facil:
            acertou = True
        else:
            if jogador > facil:
                print('Menos... tente novamente...')
            elif jogador < facil:
                print('Mais... tente novamente...')
elif escolha == 2:
    print('Você escolheu o nivel MÉDIO, vamos começar... ')
    print('Estou pensando em um número entre 0 e 10, você consegue acertar??')
    while not acertou:
        jogador = int(input('Digite seu palpite: '))
        if jogador == medio:
            acertou = True
        else:
            if jogador > medio:
                print('Menos... tente novamente...')
            elif jogador < medio:
                print('Mais... tente novamente...')
elif escolha == 3:
    print('Você escolheu o nivel DIFIL, vamos começar... ')
    print('Estou pensando em um número entre 0 e 15, você consegue acertar??')
    while not acertou:
        jogador = int(input('Digite seu palpite: '))
        if jogador == dificil:
            acertou = True
        else:
            if jogador > dificil:
                print('Menos... tente novamente...')
            elif jogador < dificil:
                print('Mais... tente novamente...')
print('Você acertou!!')

