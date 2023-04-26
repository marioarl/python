#crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre
#a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
#usuario se ele quer ou nao continuar a digitar

#minha resposta
""""
cont = soma = maior = menor = 0
opc = "S"
while opc in "S":
    num = int(input("Digite um numero: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opc = str(input("Continua? [S/N] ")).strip().upper
media = soma / cont
print(f"Voce digitou {cont} numeros e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
"""


#resposta do Gustavo
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))