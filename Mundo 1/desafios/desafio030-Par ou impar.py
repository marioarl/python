#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR

#Minha resposta
numero = int(input('Me diga um número qualquer: '))
if numero % 2 == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))

#Resposta do Gustavo
numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))
