from datetime import datetime
funcionario = dict()

funcionario['Nome'] = input('Nome: ')
funcionario['Ano de nascimento'] = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - funcionario['Ano de nascimento']
funcionario['Carteira de trabalho'] = int(input('Carteira de trabalho (Digite 0 se não tiver): '))
if funcionario['Carteira de trabalho'] != 0:
    funcionario['Ano de contratação'] = int(input('Ano de contratação: '))
    funcionario['Salario'] = float(input('Salário: R$ '))
    funcionario['Aposentadoria'] = funcionario['idade'] + ((funcionario['Ano de contratação'] + 35) -
                                                           datetime.now().year)
print('='*30)
print(f'>>> Funcionário(a): {funcionario["Nome"]}')
print(f'>>> Idade: {funcionario["idade"]}')
if funcionario['Carteira de trabalho'] > 0:
    print(f'>>> CTPS: {funcionario["Carteira de trabalho"]}')
    print(f'>>> Contratação foi em: {funcionario["Ano de contratação"]}')
    print(f'>>> Salário: R$ {funcionario["Salario"]}')
    print(f'>>>O funcionário irá se aposentar com {funcionario["Aposentadoria"]} anos')
else:
    print(f'>>> CTPS: O funcionário não possui CTPS')

