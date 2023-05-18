#Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo

#minha resposta igual do Gustavo
numero = int(input('Digite um Numero: '))
tot = 0
for num in range(1, numero + 1):
    if numero % num == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(num), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')