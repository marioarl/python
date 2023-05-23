'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
o usuario vai continuar. No final mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
'''

#minha resposta
"""print('-'*30)
print('{:^30}'.format('LOJAS SUPER BARATÃO'))
print('-'*30)
total = mais = menor = conta = 0
listam = []
lista = []
listap = []
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    lista.append(produto)
    lista.append(preco)
    conta += 1
    total += preco
    if conta == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 100:
        mais += 1
        listam.append(produto)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-'*30)
    if cont == 'N':
        break
print('-'*30)
print(f'{"LISTA DE ITENS COMPRADOS":^30}')
print('-'*30)
print(f'\033[31m{"ITEM":<20}\033[m', end='')
print(f'\033[31m{"PRECO"}\033[m')
for l in range(0, len(lista)):
    if l %2 == 0:
        print(f'{lista[l]:.<20}', end='')
    else:
        print(f'R${lista[l]:>7.2f}')
print()
print('-'*7, "RESUMO DA COMPRA", '-'*7)

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais} produtos custando mais de R$100.00, que são: ', end='')
for c in listam:
    print(f'{c}, ', end='')
print(f'\nO produto mais barato foi \033[33m{barato}\033[m e custa R${menor:.2f}')"""
#resposta do Gustavo
total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que cussta R${menor:.2f}')
