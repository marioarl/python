# faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

#minha resposta
print('', '\033[1;34m-'*40, '\n', '|', '\033[7;33m          TABUADA DOS NUMEROS        \033[m\033[1;34m|')
print('', '-'*40, '\033[m')
n = int(input('\033[1;31mEscolha um numero: \033[m'))
print('{} X {:2} ={}'.format(n, 1, n*1))
print('{} X {:2} = {}'.format(n, 2, n*2))
print('{} X {:2} = {}'.format(n, 3, n*3))
print('{} X {:2} = {}'.format(n, 4, n*4))
print('{} X {:2} = {}'.format(n, 5, n*5))
print('{} X {:2} = {}'.format(n, 6, n*6))
print('{} X {:2} = {}'.format(n, 7, n*7))
print('{} X {:2} = {}'.format(n, 8, n*8))
print('{} X {:2} = {}'.format(n, 9, n*9))
print('{} X {:2} = {}'.format(n, 10, n*10))
print ('\033[1;34m-'*40)