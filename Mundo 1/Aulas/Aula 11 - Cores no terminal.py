# Cores no terminal
# Exemplo: \033[0;33;44m onde:
# \033[ ==> ANSI escape sequence
# 0 ==> ESTILO
# 33 ==> TEXTO
# 44 ==> Background

# ESTILO = 0 - None , 1 - Bold, 4 - Underline, 7 - Negativo
# TEXTO  = 30 - Branco, 31 - Vermelho, 32 - Verde, 33 - Amarelo, 34 - Azul, 35 - magenta, 36 - Ciano, 37 - Cinza
# BG     = 40 - Branco, 41 - Vermelho, 42 - Verde, 43 - Amarelo, 44 - Azul, 45 - Magenta, 46 - Ciano, 47 - Cinza             
# Para delimitar onde termina o escape sequence, devemos colocar \033[m

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
