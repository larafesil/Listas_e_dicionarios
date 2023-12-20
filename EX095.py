time = list()
lista = dict()
partidas = list()
while True:
    lista.clear()
    lista['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {lista["nome"]} jogou: '))
    partidas.clear()
    for num in range(0, jogos):
            partidas.append(int(input(f'    Quantos gols na {num+1}ª partida: ')))
    lista['gols'] = partidas[:]
    lista['total'] = sum(partidas)
    time.append(lista.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N!')
    if resp == 'N':
        break
print('.'*50)
print('cod ', end='')
for i in lista.keys():
    print(f'{i:<15}', end='')
print()
print('.'*50)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('.'*50)
