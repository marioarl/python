'''
Escreva um programa que leia dois numeros inteiros  e compare-os, mostrando na tela uma
mensagem:
O primeiro valor é maior
o segundo valor é maior
nao existe valor maior, os dois sao iguais
'''

#Minha resposta
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num1 < num2:
    print('O SEGUNDO valor é maior')
elif num1 == num2:
    print('Os dois valores são IGUAIS')

#Resposta do Gustavo
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
