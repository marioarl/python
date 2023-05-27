'''crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma lista unica que
mantenha separados os valores PARES e IMPARES. No final, mostre os valores pares e impares em ordem crescente'''

#minha resposta
numeros = list()
pares = list()
impares = list()
for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}o. valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
numeros.append(pares)
numeros.append(impares)
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')

#resposta Gustavo
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='* 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')