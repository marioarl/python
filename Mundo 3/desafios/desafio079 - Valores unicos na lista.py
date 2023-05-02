#crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma
#lista. Caso o numero já exista lá dentro, ele nao será adicionado. No final serao exibidos todos
#os valores unicos digitados em ordem crescente
#minha resposta
num = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=-'*15)
num.sort()
print(f'Voce digitou os valores {num}')

#resposta do Gustavo
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
