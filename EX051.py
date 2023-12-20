print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razão
for c in range(primeiro_termo, decimo + razão, razão):
    print(c, '➾ ', end='')
print('ACABOU')