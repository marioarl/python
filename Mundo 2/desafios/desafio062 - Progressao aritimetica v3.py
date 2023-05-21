'''Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0(zero) termos.'''

print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))