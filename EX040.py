aluno = str(input('Aluno(a): '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.00:
    print('A média do aluno foi {:.1f}. REPROVADO'.format(media))
elif 7 > media >= 5:
    print('A média do aluno foi {:.1f}. RECUPERAÇÃO'.format(media))
elif media >= 7.00:
    print('A média do aluno foi {:.1f}. APROVADO'.format(media))