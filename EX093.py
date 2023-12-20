lista = dict()
partidas = list()
lista['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {lista["nome"]} jogou: '))
for num in range(0, jogos):
        partidas.append(int(input(f'    Quantos gols na {num+1}ª partida: ')))
lista['gols'] = partidas[:]
lista['total'] = sum(partidas)
print('.'*50)
print(lista)
print('.'*50)
for k, v in lista.items():
        print(f'>>> {k} = {v}')
print('.'*50)
print(f'O jogador {lista["nome"]} jogou {jogos} partidas')
for i, v in enumerate(lista['gols']):
        print(f'        => Na partida {i+1}, fez {v} gols')
print(f'Total de gols = {lista["total"]}')

