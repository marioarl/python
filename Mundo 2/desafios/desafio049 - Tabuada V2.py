'''
Refaça o DESAFIO09, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço FOR
'''

#Minha Resposta
from time import sleep
print('\033[34m-\033[m'*40,'\n\033[34m|\033[m', end=' ')
print('\033[7;33m{:^48}'.format('TABUADA DOS NUMEROS         \033[m', '|'))
print('\033[34m-\033[m'*40)
n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print('{:^10} X {:^10} = {:^10}'.format(n, c, n*c))
    sleep(0.5)
print('\033[34m-\033[m'*40)

