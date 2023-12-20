# CONTADORES
gastos_total = 0
produtos_mais_mil = 0
menor_preço = 0
contador = 0
produto_mais_barato = ' '

# VARIAVEIS DE DESING
var1 = '='
var2 = 'LOJA SUPER BARATÃO'
print(var1 * 30)
print(f'{var2:^28}')
print(var1 * 30)
while True:
    produto = input('Produto: ')
    preço = float(input('Valor: R$ '))
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S / N]? ').upper().strip()[0]
    gastos_total += preço
    if preço >= 1000:
        produtos_mais_mil += 1
    if contador == 1 or preço < menor_preço:
        menor_preço = preço
        produto_mais_barato = produto
    print(var1 * 30)
    if continuar == 'S':
        continue
    else:
        break
print(f'O produto mais barato é {produto_mais_barato} e custa R$ {menor_preço:.2f}')
print(f'{produtos_mais_mil} produtos custam mais de R$ 1.000,00')
print(f'O total da compra é R$ {gastos_total:.2f}')