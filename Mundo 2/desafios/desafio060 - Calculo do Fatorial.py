'''
Faça um programa que leia um numero qualquqer e mostre seu fatorial
EX: 5!=5X4X3X2X1 = 120
'''
print('Digite um numero para')
num = int(input('calcular seu fatorial: '))
fat2 = 0
for c in range(1, num, -1):
    fat = num * c
    print('Calculando {}! = {} X {}'.format(num, num, c))

#resposta1 Gustavo(com modulo math
#from math import factorial
#n = int(input('Digite um número para calcular seu fatorail: '))
#f = factorial(n)
#print('O fatorial de {} é {}'.format(n, f))

#resposta2 Gustavo
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))




