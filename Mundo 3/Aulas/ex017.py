num = [2, 5, 9, 1]
num[2] = 3 #alterada a posicao 2 da (9) para o numero (3)
num.append(7) # adiciona o numero (7) na lista
num.sort() # coloca os numeros em ordem
#num.sort(reverse=True) # coloca os numeros de tras para frente
num.insert(2, 0) #adiciona o numero (0) na posicao 2 da lista
num.pop() # elimina o ultimo elemento da lista (1)
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('\033[33m*\033[m'*40)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2) #adicionando um elemento já existente na lista
num.remove(2) #remove somente o primeiro numero (2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('\033[33m*\033[m'*40)

#se voce remover um elemento que nao existe, o Python vai mostrar um erro, mas é possivel como o uso do IF

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4) #o elemento 4 nao existe na lista
else:
    print('Nao achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('\033[33m*\033[m'*40)

valores = [] # pode-se comecar uma lista vazia tambem com valores = list()
valores.append(5) # adiciona valores na lista
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')



valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):# mostra o indice(c) de cada elemento(v)
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
print('\033[33m*\033[m'*40)


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:'))) # coloca valores na lista atraves de um input
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
print('\033[33m*\033[m'*40)

a = [2, 3, 4, 7]
b = a #ligacao de lista
b[2] = 8 # se é igualada uma lista com a outra, muda o valor das duas listas
print (f'Lista A: {a}')
print(f'Lista B: {b}')
print('\033[33m*\033[m'*40)

a = [2, 3, 4, 7]
b = a[:] # copiar todos os valores da lista a e colocar em b, criando uma cópia
b[2] = 8
print (f'Lista A: {a}')
print(f'Lista B: {b}')
print('\033[33m*\033[m'*40)