from math import sin,cos,tan,radians
print('SENO, COSSENO E TANGENTE')
a = float(input('Digite o ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {}º tem o seno de {:.2f}º'.format(a,s))
print('O ângulo de {}º tem o cosseno de {:.2f}º'.format(a,c))
print('O ângulo de {}º tem a tangente de {:.2f}º'.format(a,t))
