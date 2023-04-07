#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex. Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

#minha resposta
num = str(input('Digite um numero: ')).strip()
lista_num = list(num)
print(f'Unidade.: {lista_num[3]}')
print(f'Dezena..: {lista_num[2]}')
print(f'Centena.: {lista_num[1]}')
print(f'Milhar..: {lista_num[0]}')

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