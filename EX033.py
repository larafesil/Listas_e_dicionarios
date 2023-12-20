v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
max = v1
# se v2 for maior que a variavel max que é igual a v1, então o 'max' se torna v2.Vale o mesmo para o v3
if v2 > max:
    max = v2
if v3 > max:
    max = v3
min = v1
# se v2 for menor que a variavel min que é igual a v1, então o 'min' se torna v2. vale o mesmo para o v3
if v2 < min:
    min = v2
if v3 < min:
    min = v3
print('O maior valor digitado foi {}'.format(max))
print('O menor valor digitado foi {}'.format(min))
