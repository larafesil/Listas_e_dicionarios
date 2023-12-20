from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
ranking = list
print('Valores sorteados')
for c, i in dados.items():
    print(f'O {c} tirou {i} no dados')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1),reverse=True)
print('='*30)
print(F'{"RANKING":^30}')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
