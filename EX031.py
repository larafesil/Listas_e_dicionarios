km = float(input('Qual a distância da sua viagem? '))
if km <= 200:
    print('Você está prestes a começar uma viagem de {}Km'.format(km))
    print('O preço da viagem será de R$ {:.2f}'.format(km * 0.50))
else:
    print('Você está prestes a começar uma viagem de {}Km'.format(km))
    print('O preço da viagem será de R$ {:.2f}'.format(km * 0.45))