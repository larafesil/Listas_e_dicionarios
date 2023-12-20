# VARIAVEIS DE DESING
var1 = '='
var2 = 'BANCO LABANK'

print(var1 * 30)
print(f'{var2:^30}')
print(var1 * 30)
print('''CÉDULAS DISPONIVEIS:
R$ 100,00
R$ 50,00
R$ 20,00
R$ 10,00
R$ 1,00''')
valor = int(input('Valor a ser sacado: '))
total = valor
ced = 50
total_cedulas = 0
while True:
    if total >= ced:
        total -= ced
        total_cedulas += 1
    else:
        print(f'Total de {total_cedulas} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedulas = 0
        if total == 0:
            break