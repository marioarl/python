'''Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma TUPLA.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor valor e o maior valor que
estao na TUPLA'''

#minha resposta
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(n, end= ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

#resposta do Gustavo

#from random import randint
#numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#print('Os valores sorteados foram:', end=' ')
#for n in numeros:
#    print(f'{n}', end=' ')
#print(f'\nO maior valor sorteado foi {max(numeros)}')
#print(f'O menor valor sorteado foi {min(numeros)}')

