print('DESCONTOS EM PRODUTOS')
print()
p = input('Produto: ')
v = float(input('Valor: R$ '))
d = v * 0.05
vcd = v - d
print('Valor do produto com desconto: {:.2f}'.format(vcd))
print('O valor do desconto foi de R$ {:.2f}'.format(d))