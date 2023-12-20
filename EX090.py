aluno = {}
media = []
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'Aluno(a): {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]}')
if aluno['Média'] >= 7.0:
    print('Situação igual a APROVADO')
else:
    print('Situação igual a REPROVADO')