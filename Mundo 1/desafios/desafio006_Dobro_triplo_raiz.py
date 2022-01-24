# Crie um  algoritmo que leia um numero e mostre o seu dobro, o triplo e raiz quadrada

# Minha solucao
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verdepreto':'\033[7;32m',
         'magpreto':'\033[7;35m',
         'verde':'\033[32m',
         'azulpreto':'\033[7;34m'}
print('\033[1;35m='*20, '\033[7;35mANALISE DE NUMERO\033[m', '\033[1;35m=\033[m'*20)
n = int(input('\033[1;31mDigite um numero:\033[m '))
print('O dobro de {} vale: {}{}{}'.format(n, cores['verdepreto'], n * 2, cores['limpa']))
print('O triplo de {} vale: {}{}{}' .format(n, cores['magpreto'], n*3, cores['limpa']))
print('A raiz quadrada de {} vale: {}{:.2f}{}'.format(n, cores['azulpreto'], n**(1/2), cores['limpa']))


#Resposta do Gustavo
#n = int(input('Digite um numero: '))
#print('O dobro de {} vale {}'.format(n, (n*2)))
#print('O triplo de {} vale {}\nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, pow(n, (1/2))))