# VARIANTE PARA ARMAZENAR DADOS
somalidade = 0
media_idade = 0
maior_idade_velho = 0
nome_velho = ''
cont_mulher_nova = 0
for c in range(1, 5):
    print('------- {}ª PESSOA -------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somalidade += idade  # A MEDIA VAI ARMAZENAR AS IDADES QUE SERÃO COLOCADAS
    if c == 1 and sexo in 'Mm':
        maior_idade_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_velho:
        maior_idade_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        cont_mulher_nova += 1
media_idade = somalidade / 4
print('A média de idade do grupo é de {}'.format(media_idade))
print('O homem mais velho tem {} e se chama {}'.format(maior_idade_velho, nome_velho))
print('Ao todo são {} mulheres que tem menos de 20 anos.'.format(cont_mulher_nova))


