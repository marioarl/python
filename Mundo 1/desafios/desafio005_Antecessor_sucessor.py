'''faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e sue antecessor
'''
#minha resposta
print('\033[1;32m=-'*10, '\033[7mANALISE DE NUMERO\033[m', '\033[1;32m-=\033[m'*10)
n = int(input('\033[1;34mDigite um numero:\033[m '))
s = n + 1
a = n - 1
print('\033[31mO numero é\033[m \033[4;31m{}\033[m \n\033[33mO sucessor é\033[m \033[4;33m{}\033[m'
      ' \n\033[35mO antecessor é\033[m \033[4;35m{}'.format(n, s, a))

#resposta do Gustavo
n = int(input('Digite um numero: '))
print ('Analisando o valor{}, seu antecessor é {} e o sucessor é {}'.format (n, (n-1), (n+1)))