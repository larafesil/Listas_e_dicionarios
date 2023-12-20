frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()   # LISTA DAS PALAVRAS DA FRASE
junto = ''.join(palavras)  # JUNTA EM UMA STR SÓ
inverso = ''
# print('O inverso de {} é {}'.format(junto,junto[::-1]))
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]  # INVERSO DA FRASE SEM ESPAÇOS
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase digitada é um PALINDROMO')
else:
    print('A frase digitada NÃO É UM PALINDROMO')