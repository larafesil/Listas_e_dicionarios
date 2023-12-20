print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro_termo # armazenar o primeiro termo para começar a contagem
contador = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ➾ '.format(termo), end='')
        contador += 1
        termo += razão
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais: '))


