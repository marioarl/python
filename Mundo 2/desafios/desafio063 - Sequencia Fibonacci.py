#escreva um programa que leia um numero n inteiro qulquer e mostre na tela os n primeiros
#elementos de uma sequencia fibonacci
#ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-'*40)
print('{:^40}'.format('SEQUENCIA DE FIBONACCI'))
print('-'*40)
termos = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3 # o contador será 3 porque já temos o termo 1 e o termo 2
while cont <= termos:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2 #transicão de termos
    t2 = t3 #trnasicao de termos
    cont += 1
print(' -> FIM')
