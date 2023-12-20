sair = False
contador = 0
soma = 0
while not sair:
    numero = int(input('Digite um número [999 PARA PARAR]: '))
    if numero != 999:
        contador += 1
        soma += numero
    if numero == 999:
        sair = True
print('Foram digitados {} numéros e a soma deles é {}'.format(contador, soma))
print('PROGRAMA FINALIZADO')