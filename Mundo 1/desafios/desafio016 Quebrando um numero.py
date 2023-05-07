'''
Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porçao
inteira EX: Digite o numero: 6.127 O numero 6.127 tem a parte inteira 6

'''
#minha resposta
#from math import trunc
#num = float(input('Digite o numero: '))
#parte = trunc(num)
#print('O valor digitado foi {} e sua porção inteira é {}'.format(num, parte))

#resposta 1 do Gustavo
#import math
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#resposta 2 do Gustavo
#from math import trunc
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#resposta 3 do Gustavo
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))