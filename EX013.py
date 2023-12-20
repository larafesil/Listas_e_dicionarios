print('SALÁRIO FUNCIONÁRIOS')
print()
f = str(input('Funcionário(a): '))
s = float(input('Sálario atual: '))
a = s * 0.15
ns = s + a
print('O salário atual do(a) funcionário(a) {} será de R$ {:.2f}'.format(f,ns))
print('Teve um acréscimo de R$ {:.2f}'.format(a))
