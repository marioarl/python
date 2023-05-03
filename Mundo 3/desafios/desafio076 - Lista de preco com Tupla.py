'''crie um programa que tenha uma unica TUPLA com nomes de produtos e seus respectivos precos na sequencia.
No final mostre uma listagem de precos organizando os dados em forma tabular'''
#minha resposta
print('-'*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-'*40)
lista = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for l in range(0, len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]:.<30}', end='')
    else:
        print(f'R${lista[l]:>7.2f}')
print('-'*40)

#resposta do Gustavo
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end="")
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)