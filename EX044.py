print('='* 15, 'LOJAS LAFIT', '=' *15)
compras = float(input('Preço da compras: R$ '))
print('FORMA DE PAGAMENTO')
print('''(1) à vista dinheiro/cheque
(2) à vista cartão
(3) 2x no cartão
(4) 3x ou mais no cartão''')
escolha = int(input('Qual a opção? '))
avista = compras * 0.1
avistacartão =  compras * 0.05
cartão3 = compras * 0.2
if escolha == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compras, compras - avista))
elif escolha == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compras, compras - avistacartão))
elif escolha == 3:
    print('Sua compra será parcelada em 2x de {:.2f} SEM  JUROS'.format(compras / 2))
    print('Sua compra vai sair por R$ {:.2f}'.format(compras))
elif escolha == 4:
    total = compras + cartão3
    parcelas = int(input('Quantas parcelas? '))
    totparcelas = total / parcelas
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcelas, (cartão3 + compras) / parcelas))
    print('Sua compra no valor de {:.2f} terá acréscimo de {:.2f} e irá sair por {:.2f}'.format(compras, cartão3, compras + cartão3))
else:
    print('Opção INVÁLIDA, tente novamente')