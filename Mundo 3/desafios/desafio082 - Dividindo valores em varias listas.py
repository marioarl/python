'''
Crie um programa que leia varios numeros e coloque em uma lista.
Depois disso crie 2 listas extras que vao conter apenas os valores pares e eu outra lista os valores impares
Ao final mostre o conteudo das 3 listas geradas
'''

#Minha resposta
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'A lista completa é {lista}')
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')


#resposta do Gustavo
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')





