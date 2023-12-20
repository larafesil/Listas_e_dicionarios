from random import randint

# CONTADORES
computador = randint(1,10)
contador = 0

# VARIAVEIS DE DESING
var1 = '=-'
var2 = '='
var3 = ' VAMOS JOGAR PAR OU ÍMPAR? '

print(var1 * 10, var3, var1 * 10)
print(var1 * 35)
while True:
    valor = int(input('Digite um valor: '))
    escolha = str(input('PAR OU ÍMPAR: ')).upper()
    resultado = valor + computador
    if escolha == 'PAR' or 'P':
        print(f'Você jogou {valor} e o computador {computador}. O total é {resultado}', end=' ')
        if resultado % 2 == 0:
            print('DEU PAR!! VOCÊ GANHOU!!')
            contador +=1
            print(var1 * 35)
            print('Vamos jogar novamente...')
            print(var1 * 35)
        else:
            print('DEU IMPAR!! VOCÊ PERDEU!!')
            break
    if escolha == 'IMPAR' or 'ÍMPAR' or 'I' or 'Í':
        print(f'Você jogou {valor} e o computador {computador}. O total é {resultado}', end=' ')
        if resultado % 2 == 0:
            print('DEU PAR!! VOCÊ PERDEU!!')
            break
        else:
            print('DEU IMPAR!! VOCÊ GANHOU!!')
            contador += 1
            print(var1 * 35)
            print('Vamos jogar novamente...')
            print(var1 * 35)
if contador > 0:
    print(var1 * 35)
    print(F'Você teve {contador} vitórias consecultivas. PARABÉNS')
    print(var1 * 35)
print('XXXXXXXXXXXXXXXXXXXXXXXXX JOGO FINALIZADO XXXXXXXXXXXXXXXXXXXXXXXXX')
