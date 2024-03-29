'''
Faca um programa que leia 5 valores numericos e guarde-os em uma lista
No final mostre qual foi o maior e o menor valor digitados e suas respectivas posicoes na lista
'''

#Minha resposta
num = []
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
print()

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

#Resposta do Gustavo
listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-=' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i,v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end="")
print()
print(f'O menor valor digitado foi {men} nas posições ', end="")
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end="")
print()    
