from math import pow, sqrt, hypot
'''print('CATETOS E HIPOTENUSA')
print('')
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = ((co.__pow__(2)) + (ca.__pow__(2)))
print('A hipotenusa vale {:.2f}'.format(sqrt(h)))'''

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(co,ca)
print('A hipotenusa vale {}'.format(h))