produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Eatojo', 25.00,
            'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
var1 = 'LISTA DE PRODUTOS'
print('-'*40)
print(F'{var1:^40}')
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}',end='')
    else:
        print(f'R$ {produtos[item]:>1.2f}')
print('-'*40)