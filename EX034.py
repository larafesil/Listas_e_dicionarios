nome = str(input('Funcionário(a): '))
salario = float(input('Qual o salário? '))
if salario > 1250.00:
    print('O sálario terá aumento de {:.2f}'.format(salario * 0.1))
    print('O salário total ficará {:.2f}'.format(salario + (salario * 0.1)))
else:
    print('O sálario terá aumento de {:.2f}'.format(salario * 0.15))
    print('O salário total ficará {:.2f}'.format(salario + (salario * 0.15)))