#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex. Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

#minha resposta 1(nao consegui fazer)
#num = str(input('Informe o numero: '))
#print('Analisando o numero {}'.format(num))
#print (len(num))

#resposta do Gustavo
num = int(input('Informe o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))