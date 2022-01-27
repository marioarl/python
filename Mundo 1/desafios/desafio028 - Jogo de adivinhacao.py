#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça
#para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# o computador devera escrever se o usuario venceu ou perdeu

#minha resposta
#import random
#print('-=-'*20, '\n Vou pensar em um numero entre 0 e 5. tente adivinhar...\n', '-=-'*20)
#numero = int(input('Em que numero pensei? '))
#ncomp = random.choice([1, 2, 3, 4, 5])
#print('PROCESSANDO...')
#if numero == ncomp:
#    print('PARABENS! Voce conseguiu me vencer!')
#else:
#    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(ncomp, numero))

#resposta do Gustavo
from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador escolher o numero
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivnhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))