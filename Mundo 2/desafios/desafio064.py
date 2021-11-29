#crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o
#usuario digitar o valor 999, que é a condicao de parada. No final mostre quantos numeros foram digitados
#e qual foi a soma entre eles, desconsiderando o 999.
cont = soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))