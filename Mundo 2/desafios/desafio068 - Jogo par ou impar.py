'''
Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o
jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''

from random import randint

#minha resposta
from random import randint
v = 0
print("-="*20)
print("VAMOS JOGAR PAR OU IMPAR".center(40))
print("-="*20)

while True:
    comp = randint(0,10)
    jog = int(input("Diga um valor: "))
    opc = str(input("Par ou Impar? [P/I] ")).strip().upper()
    print("-"*40)
    total = comp + jog
    print(f"Voce jogou {jog} e o computador {comp}. Total de {total} ", end="")
    if opc == "P":
        if total % 2 == 0:
            print("DEU PAR")
            print("-"*40)
            print("Voce VENCEU!")
            v += 1
        else:
            print("DEU IMPAR")
            print("-"*40)
            print("Voce PERDEU")
            break
    if opc == "I":
        if total %2 == 1:
            print("DEU IMPAR")
            print("-"*40)
            print("Voce VENCEU! ")
            v += 1
        else:
            print("DEU PAR")
            print("Voce PERDEU")
            break
print(f"GAME OVER! Voce venceu {v} vezes.")

#resposta do Gustavo
v = 0
print('=-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*15)
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in ('PI'):
        tipo = str(input('par ou impar? [P/I] ')).strip().upper()
    print(f'Voce jogou {jogador} e o computador {comp}. Total de {total}', end=' ')
    print('DEU PAR' if total %2 == 0 else 'DEU IMPAR' )
    if tipo == 'P':
        if total %2 == 0:
            print('Voce Venceu!')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Voce Venceu')
            v +=1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER. Voce venceu {v} vezes')
