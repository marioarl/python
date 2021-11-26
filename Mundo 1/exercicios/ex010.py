print('\033[4;30;45mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[31m{}\033[m e \033[35m{}\033[m!!!'.format(a, b))


nome = 'Mario'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4:34m', nome, '\033[m'))

#outra forma de colocar cores (colecao)
nome = 'Mario'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))
