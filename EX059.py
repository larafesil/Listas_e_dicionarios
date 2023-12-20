from time import sleep
sair_do_programa = False
primeiro_num = int(input('Digite o primeiro número: '))
segundo_num = int(input('Digite o segundo número: '))
while not sair_do_programa:
    sleep(1)
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    opção = str(input('>>>>>>>> Digite sua opção: '))
    print('-==-==-==-==-==-==-==-==-==-==-==-==-==-')
    if opção == '1':
        result = primeiro_num + segundo_num
        print('{} + {} = {}'.format(
                primeiro_num,segundo_num,result))
    elif opção == '2':
        result = primeiro_num * segundo_num
        print('{} x {} = {}'.format(
                primeiro_num,segundo_num,result))
    elif opção == '3':
        if primeiro_num > segundo_num:
            print('Entre {} e {} o maior é {}'.format(
                    primeiro_num, segundo_num, primeiro_num))
        else:
            print('Entre {} e {} o maior é {}'.format(
                    primeiro_num, segundo_num, segundo_num))
    elif opção == '4':
          primeiro_num = int(input('Digite o primeiro número: '))
          segundo_num = int(input('Digite o segundo número: '))
    elif opção == '5':
        sair_do_programa = True
        print('xxxxxxxxxxxxxx FIM xxxxxxxxxxxxxx')
    else:
        print('Opção inválida, tente novamente!!')
        