import datetime
maiores = 0
menores =  0
for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        maiores = maiores + 1
    elif idade < 18:
        menores = menores + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('Ao todo tivemos {} pessoas menores de idade'.format(menores))