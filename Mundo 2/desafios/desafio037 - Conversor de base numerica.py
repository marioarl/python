'''
Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será
a base de conversao:
1 binario     2 octal     3 hexadecimal
'''

#Minha resposta
num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
bin = bin(num)
oc = oct(num)
hexa = hex(num)
opcao = int(input('Escolha sua opcao:'))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {} '.format(num, bin[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oc[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexa[2:]))

#Resposta do gustavo
num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Escolha sua opcao:'))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {} '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')