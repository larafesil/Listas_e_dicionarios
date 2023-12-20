print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro_termo # armazenar o primeiro termo para começar a contagem
contador = 1
while contador <= 10:
    print('{} ➾ '.format(termo), end='')
    contador += 1
    termo += razão
print('ACABOU')



