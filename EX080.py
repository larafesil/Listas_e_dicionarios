numero = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0:
        numero.append(n)
        print('Adicionado no começo da lista')
    elif n > numero[-1]:
        numero.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
                numero.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os alores adicionado em ordem foram {numero}')
