n = int(input('''Digite um número para
calcular o seu Fatorial: '''))
c = n # contador que vai começar o numero factorial
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end= ' ')
    print('x 'if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)

