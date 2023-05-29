'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados
em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero
minha resposta
'''
#Minha resposta
from random import randint
from time import sleep
from operator import itemgetter #para colocar um dicionario em ordem temos que importar ITEMGETTER p func. com o SORTED
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = []# criar uma litsa para colocar em ordem, não é necessario criar dicionario
print('Valores sorteados:')
for k, i in jogadores.items():
    print(f'{k} tirou {i} no dado')
    sleep(1)
print('-='*30)
print('  ==RANKING DOS JOGADORES==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1}o. lugar: {v[0]} com {v[1]}')
    sleep(1)


#Resposta do Gustavo
jogo = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  ==RANKING DOS JOGADORES==')
for i, v in enumerate(ranking):
    print(f'  {i+1}o. lugar: {v[0]} com {v[1]}')
    sleep(1)

