'''
Crie um programa que leia nome e peso de varias pessoas guardando tudo em uma lista. No final mostre
A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas
C)Uma listagem com as pessoas mais leves
'''
#Minha Resposta
pessoas = []
unico = []
maior=menor=0
while True:
    unico.append(str(input('Nome: ')))
    unico.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = unico[1]
    else:
        if unico[1] > maior:
            maior = unico[1]
        if unico[1] < menor:
            menor = unico[1]
    opc = str(input('Continua? [S/N] ')).strip().upper()
    pessoas.append(unico[:])
    unico.clear()
    if opc == "N":
        break

print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end="")
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end="")
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end="")
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end="")
print()

#Resposta do Gustavo
dados = list()
pessoas = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in resp:
        break
print('-='*30)
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
