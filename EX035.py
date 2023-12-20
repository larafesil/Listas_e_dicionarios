print('-=' * 30)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 30)
med1 = float(input('Digite a primeira medida: '))
med2 = float(input('Digite a segunda medida: '))
med3 = float(input('Digite a terceira medida: '))
#cada medida for menor que a soma das outras duas medidas juntas
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('Pode formar um triângulo')
    if med1 == med2 == med3:
        print('EQUILÁTERO')
    if med1 != med2 != med3:
        print('ESCALENO')
    if med1 == med2 != med3 and med2 == med3 != med1
        print('ISÓSCELES')
else:
    print('Não pode formar um triângulo')