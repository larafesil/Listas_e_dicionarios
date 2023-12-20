n = 0
c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n > 0:
        for c in range(1,11):
            result = n * c
            print(f'{n} x {c} = {result}')
    if n < 0:
        break
print('PROGRAMA ENCERRADO')
