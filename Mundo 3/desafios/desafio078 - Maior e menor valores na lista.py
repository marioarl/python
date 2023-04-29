#faca um programa que leia 5 valores numericos e guarde-os em uma lista
# No final mostre qual foi o maior e o menor valor digitados e suas respectivas posicoes na lista
#minha resposta
"""num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posicao {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('='*40)
print(f'Voce digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posicoes ' , end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()"""

#Minha resposta 2 - Programa melhorado, utilizando o metodo max e min e retirando o bloco da logica para achar o maior e o menor valor
num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posicao {c}: ')))
print('='*40)
print(f'Voce digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posicoes ' , end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(num)} nas posicoes ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')
print()


