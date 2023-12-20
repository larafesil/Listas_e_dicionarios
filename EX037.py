num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolha = int(input('Digite a opção: '))
if escolha == 1:
    print('O número {} convertido em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente')
