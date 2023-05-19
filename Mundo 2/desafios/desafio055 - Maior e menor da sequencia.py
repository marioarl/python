'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

"""minha resposta
maior = menor = 0
for p in range(1,6):
    peso = float(input(f"Peso da {p}a. pessoa: "))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi de {maior:.1f}Kg")
print(f"O menor peso lido foi de {menor:.1f}Kg")"""

#resposta Gustavo
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}a. pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

