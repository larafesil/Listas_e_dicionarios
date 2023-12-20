import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - ano
if idade == 18:
    print('Quem nasceu em {} tem {} em {}.'.format(ano, idade, datetime.date.today().year))
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade < 18:
    print('Quem nasceu em {} tem {} em {}.'.format(ano, idade, datetime.date.today().year))
    print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + 18))
elif idade > 18:
    print('Quem nasceu em {} tem {} em {}.'.format(ano, idade, datetime.date.today().year))
    print('Você devia ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))