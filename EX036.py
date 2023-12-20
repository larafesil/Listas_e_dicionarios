print('-=' * 20)
print('PROGRAMA MINHA CASA MINHA VIDA')
print('-=' * 20)
comprador = str(input('Olá, como posso te chamar? '))
ValorDaCasa = float(input('Valor da casa: R$ '))
salario = float(input('Digite seu salário {}: R$ '.format(comprador)))
financiamento = int(input('Quantos anos de financiamento? '))
prestação = ValorDaCasa / financiamento / 12
if ValorDaCasa / financiamento / 12 <= salario * 0.3:
    print('{}, para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(comprador, ValorDaCasa,
                                                                                           financiamento, prestação))
    print('Empréstimo pode ser \033[1;32mCONCEDIDO\033[m')
else:
    print('{}, para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(comprador, ValorDaCasa,
                                                                                           financiamento, prestação))
    print('Empréstimo \033[1;31mNEGADO\033[m')