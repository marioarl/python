'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

#Minha resposta
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

#resposta do Gustavo(utilizando o operador in)
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))