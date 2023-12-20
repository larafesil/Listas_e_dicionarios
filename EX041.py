import datetime
print('Confederação Nacional de Natação')
print('''CATEGORIAS
[] MIRIM
[] INFANTIL
[] JÚNIOR
[] SÊNIOR
[] MASTER''')
data = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - data
if idade <= 9:
    print('Você vai participar da categoria: MIRIM')
elif idade <= 14:
    print('Você vai participar da categoria: INFANTIL')
elif idade <= 19:
    print('Você vai participar da categoria: JÚNIOR')
elif idade <= 25:
    print('Você vai participar da categoria: SÊNIOR')
else:
    print('Você vai participar da categoria: MASTER')
