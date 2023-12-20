print('DESAFIO 007')
print()
aluno = input('Aluno: ')
p = float(input('Nota parcial: '))
b = float(input('Nota bimestral: '))
m = (p+b)/2
print('A média do aluno {} é {:.1f}'.format(aluno,m))