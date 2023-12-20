nome = []
nota1 = nota2 = 0
ficha_alunos = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha_alunos.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar? [S/N] => ').strip()[0].upper()
    if continuar == 'S':
        continue
    else:
        break
print('='*100)
print(f'{"No.":<4}{"NOME":<40}{"MEDIA":>45}')
print('='*100)
for i, a in enumerate(ficha_alunos):
    print(f'{i:<4}{a[0]:<40}{a[2]:>45.1f}')
while True:
    print('=' * 30)
    print('''Escolha uma opção:
    
    [ 1 ] MOSTRAR NOTAS DETALHADAS
    [ 2 ] VER A LISTA DE ALUNOS NOVAMENTE
    [ 3 ] ENCERRAR PROGRAMA
    ''')
    opc = int(input('Digite a opção desejada: '))
    if opc == 1:
        print('DETALHAR NOTAS DO ALUNO')
        aluno = int(input('Digite o número do aluno correspondente a lista: '))
        if aluno <= len(ficha_alunos):
            print(f'Notas de {ficha_alunos[aluno][0]} são {ficha_alunos[aluno][1]}')
    if opc == 2:
        print('=' * 100)
        print(f'{"No.":<4}{"NOME":<40}{"MEDIA":>45}')
        print('=' * 100)
        for i, a in enumerate(ficha_alunos):
            print(f'{i + 1:<4}{a[0]:<40}{a[2]:>45.1f}')
    if opc == 3:
        print('FINALIZANDO...')
        break


