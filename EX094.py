# LISTAS E DICIONÁRIOS
lista = list()
mulheres = list()
dicionario = dict()

# VARIAVÉIS
continuar = ''
soma = 0
media = 0

# LAÇOS
while True:
    dicionario['nome'] = str(input('Nome: '))
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dicionario['sexo'] in 'MF':
            break
        print('ERRO! Utilize apenas M ou F!')
    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    while True:
        continuar = str(input('Quer continuar [S/N] =>  ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Utileze apenas S ou N!')
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
media = soma / len(lista)
print(f'>> O grupo tem {len(lista)} pessoas.')
print(f'>> A média de idade é de {media:.2f} anos.')
print(f'>> As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'],end=' ')
print()
print('>> Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print(f'>> Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')
print('<< ENCERRADO >>')
