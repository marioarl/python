#crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o
#usuario digitar o valor 999, que é a condicao de parada. No final mostre quantos numeros foram digitados
#e qual foi a soma entre eles, desconsiderando o 999.

""""
Minha resposta
cont = soma = 0
num = int(input("Digite um numero [999 para parar]: "))
while num != 999:
    cont+=1
    soma += num
    num = int(input("Digite um numero [999 para parar]: "))
print(f"Voce digitou {cont} numeros e a soma entre eles foi {soma}")

"""

#Resposta
cont = soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))