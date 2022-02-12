#cont = 1
#while cont <= 10: #condicao para a estrutura while parar até 10
#    print(cont, '->', end='')
#    cont +=1
#print('Acabou')

#cont = 1
#while True: #condicao para a estrutura while continuar INFINITO
#    print(cont, '->', end='')
#    cont +=1
#print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break #comando para parar o while e seguir
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # atualizacao Fstrings a partir do Python 3.6 interpolacao


nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos.') # PHYTHON 3.6+
print('O {} tem {} anos'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.'% (nome, idade)) # #PHYTON 2