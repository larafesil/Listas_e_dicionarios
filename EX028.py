from random import choice
from time import sleep
print('\033[4;36;40m-=-=-=-=-=-=-=-=-=-=-=-=JOGO DA ADVINHAÇÃO=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[33m=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=\033[m')
print('\033[1;30mESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 5. TENTE ADIVINHAR...\033[m')
print('\033[33m=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=\033[m')
num = int(input('\033[1;30mEm que número estou pensando?\033[m '))
numcompt = choice([0,1,2,3,4,5])
print('\033[4;34mPROCESSANDO...\033[m')
sleep(3)
if num == numcompt:
    print('\033[1;32mAFFF!! VOCÊ GANHOU!!! EU ESTAVA PENSANDO NO NÚMERO {} MESMO.\033[m'.format(num))
else:
    print('\033[1;31mHAHA VOCÊ PERDEU, EU ESTAVA PENSANDO NO NÚMERO {}.\033[m'.format(numcompt))
