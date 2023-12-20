resposta = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
while resposta == 'S':
    numero = int(input('Digite um número: '))
    contador += 1
    soma += numero
    resposta = input('Você quer continuar [SIM/NÃO]? ').upper().strip()[0]
    media = soma / contador
    if contador == 1:
        maior = numero
    if numero > maior:
        maior = numero
    if contador == 1:
        menor = numero
    if numero < menor:
        menor = numero
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
print('A média dos números digitados é igual a {}'.format(media))
print('A soma dos numeros digitados é igual a {}'.format(soma))
print('PROGRAMA ENCERRADO')