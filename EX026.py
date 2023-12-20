frase = str(input('Escreva uma frase: ')).upper().strip()
print('A letras A aparece {} vezes'.format(frase.count('A')))
print('A letras A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letras A aparece a ultima vez na posição {}'.format(frase.rfind('A')+1))