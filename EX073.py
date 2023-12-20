var1 = '=-'
lista_brasileirão = ('Palmeiras','Botafogo','Atlético-MG','Flamengo','Grêmio',
                     'Red Bull Bragantino','Fluminense','Athletico-PR','São Paulo',
                     'Internacional','Cuiabá','Corinthians','Fortaleza','Cruzeiro',
                     'Santos','Vasco','Bahia','Goiás','Coritiba','América-MG')
print(F'Lista de times do BRASILEIRÃO: {lista_brasileirão}')
print(var1 * 30)
print(f'Os 5 primeiros são: {lista_brasileirão[0:6]}')
print(var1 * 30)
print(f'Os últimos 4 são: {lista_brasileirão[-4:]}')
print(var1 * 30)
print(f'Times em ordem alfabética: {sorted(lista_brasileirão)}')
print(var1 * 30)
posição_cor = lista_brasileirão.index('Corinthians')
print(f'O Corinthians está na {posição_cor + 1}ª posição')
