'''
Crie um programa que leia varios numeros e colocar em uma lista. Depois disso mostre:
A) Quantos numeros forma digitados
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou nao na lista
'''

#minha resposta
num = []
while True:
    num.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
num.sort(reverse=True)
print(f'Voce digitou {len(num)} elementos.')
print(f'Os valores em ordem decrescente são: {num}')
if 5 in num:
    print('O numero 5 está na lista')
else:
    print('O numero 5 nao está na lista')

#resposta do Gustavo(esta resposta nao contempla se a pessoa apertar outra letra na pergunta
#'Quer continuar? [S/N]', porque se digitar qualquer letra ele aceita como S
valores = []
while True:
    valores.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')



