'''
Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
   ___________________    No final mostre a matriz na tela, com a formatacao correta
  0|     |     |     |
   |_____|_____|_____|
  1|     |     |     |
   |_____|_____|_____|
  2|     |     |     |
   |_____|_____|_____|
      0     1      2
'''
#Minha resposta
num = [[], [], []]
for n in range(0, 3):
    valor = int(input(f'Digite um valor para [0, {n}]: '))
    num[0].append(valor)
for n in range(0, 3):
    valor = int(input(f'Digite um valor para [1, {n}]: '))
    num[1].append(valor)
for n in range(0,3):
    valor = int(input(f'Digite um valor para [2, {n}]: '))
    num[2].append(valor)
print('-='*30)
print(f'[  {num[0][0]:^5}  ]', f'[  {num[0][1]:^5}  ]', f'[  {num[0][2]:^5}  ]')
print(f'[  {num[1][0]:^5}  ]', f'[  {num[1][1]:^5}  ]', f'[  {num[1][2]:^5}  ]')
print(f'[  {num[2][0]:^5}  ]', f'[  {num[2][1]:^5}  ]', f'[  {num[2][2]:^5}  ]')

#Resposta Gustavo
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
