'''
Aprimore o desafio086 mostrando no final:
A) A soma de todos os valores pares digitados:
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha
'''

#Minha resposta
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
sumpares = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            sumpares += matriz[l][c]
            pares.append(matriz[l][c])
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {sumpares}')
sum = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {sum}')
maior = max(matriz[1])
print(f'O maior valor da segunda linha é {maior}')

#Resposta Gustavo
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol =0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')