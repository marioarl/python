#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar
# quando o usuario digitar o valor 999, que é a condicao de parada . No final mostre quantos
#numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
#minha resposta
cont = soma = 0
while True:
    numero = int(input('Digite um valor (999 para parar: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')

#resposta do Gustavo
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont +=1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')


