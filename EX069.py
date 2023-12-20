# CONTADORES
pessoas_mais_18 = 0
homens = 0
mulheres_menos_20 = 0

# VARIAVEIS DE DESING
var1 = '='
var2 = '-'

while True:
    print(var1 *20)
    print('CADASTRE UMA PESSOA')
    print(var1 *20)
    idade = int(input('Idade: '))
    if idade >= 18:
        pessoas_mais_18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M / F]: ').upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = input('Deseja continuar? ').upper()
    if continuar == 'SIM':
        continue
    if continuar == 'NÃO':
        break
print(var1 *56)
print(f'''>>> Foram cadastrados {pessoas_mais_18} pessoas que tem mais de 18 anos.
>>> {homens} homens foram cadastrados.
>>> {mulheres_menos_20} mulheres tem menos de 18 anos.''')
print(var1 *56)
print('PROGRAMA FINALIZADO')