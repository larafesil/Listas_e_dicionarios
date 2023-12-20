maior = 0
menor = 0
for c in range(1,6):
    peso_pessoa = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso_pessoa
        menor = peso_pessoa
    else:
        if peso_pessoa > maior:
            maior = peso_pessoa
        if peso_pessoa < menor:
            menor = peso_pessoa
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))