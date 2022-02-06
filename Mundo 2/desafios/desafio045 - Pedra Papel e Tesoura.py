#crie um programa que faca o computador jogar JOKENPO com voce.
#import time
#import random
#print('''Suas opções:
#[ 0 ] PEDRA
#[ 1 ] PAPEL
#[ 2 ] TESOURA''')
#jogada = int(input('Qual é a sua jogada? '))
#comp = random.choice([0, 1, 2])
#lista = ('Pedra', 'Papel', 'Tesoura')
#print('JO')
#time.sleep(1)
#print('KEN')
#time.sleep(1)
#print('PO!!!')
#print('-='*20)
#print('Computador jogou {}'.format(lista[comp]))
#print('Jogador jogou {}'.format(lista[jogada]))
#print('-='*20)
#if jogada == comp:
#    print('EMPATE')
#elif jogada == 0 and comp == 1:
#    print('COMPUTADOR VENCE')
#elif jogada == 0 and comp == 2:
#    print ('JOGADOR VENCE')
#elif jogada == 1 and comp == 2:
#    print('COMPUTADOR VENCE')
#elif jogada == 1 and comp == 0:
#    print('JOGADOR VENCE')
#elif jogada == 2 and comp == 0:
#    print('COMPUTADOR VENCE')
#elif jogada == 2 and comp == 1:
#    print('JOGADOR VENCE')

#resposta Gustavo
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 } TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')