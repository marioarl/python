'''
Crie um programa que tenha uma TUPLA totalmemte preenchida com uma contagem por extenso, de
zero até vinte.
Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso
'''

#Minha resposta
extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'QUinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
digit = int(input('Digite um numero entre 0 e 20: '))
while True:
    if digit < 0 or digit > 20:
        digit = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    else:
        break
print(f'Voce digitou o numero {extenso[digit]}')

#Resposta do Gustavo
cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'QUinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        break
    print('tente novamente.', end='')
print(f'Voce digitou o numero {cont[num]}')