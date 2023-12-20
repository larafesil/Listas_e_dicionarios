lista = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
         'dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete',
         'dezoito','dezenove', 'vinte')
continuar = ' '
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        print(f'Você escolheu o número {lista[numero]}')
        continuar = str(input('Você quer continuar [ S / N ]? ')).strip()[0].upper()
        if continuar == 'S':
            continue
        else:
            print('PROGRAMA FINALIZADO')
            break
    else:
        print('Opção inválida.', end= ' ')

