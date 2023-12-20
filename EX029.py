print('Bem vindo a central de multas do Brasil Cemulbra')
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade < 80:
    print('Tenha um bom dia! Dirija com segurança!!!')
else:
    print('MULTADO! você excedeu o limite permitido que é de 80km/h.')
    print('Você deve pagar uma multa de R$ {:.2f}'.format(7 * (velocidade - 80)))