from time import sleep
from random import randint
import emoji
tentativas = 0
print('\033[33m-=\033[m'*30)
print('\033[34mVou pensar em um numero entre 0 e 5.Tente adivinhar...')
print('\033[33m-=\033[m'*30)
numero = int(input('Em que numero pensei? '))
tentativas = tentativas + 1
comp = randint(0, 10)
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
while numero != comp:
    if numero < comp:
        print('Mais...Tente mais uma vez', end=' ')
        print(emoji.emojize(':grimacing:', use_aliases=True))
        numero = int(input('Qual é o seu palpite? '))
        tentativas = tentativas + 1
    else:
        print('Menos...tente mais uma vez')
        print(emoji.emojize(':expressionless:', use_aliases=True))
        numero = int(input('Qual é o seu palpite? '))
        tentativas = tentativas + 1
if tentativas == 1:
    print('Acertou em {} tentativa, PARABENS!'.format(tentativas))
else:
    print('Acertou em {} tentativas, PARABENS!'.format(tentativas))


#resposta do gustavo
from random import randint
computador = randint(0, 10)
print('Sou seu computador....Acabei de pensar em um numero entre 0 e 10')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabens!'.format(palpites))
