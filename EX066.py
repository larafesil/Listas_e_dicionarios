n = s = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s = s + n
    c += 1
print(f'Foram digitados {c} números e a soma entre eles é igual a {s}')
