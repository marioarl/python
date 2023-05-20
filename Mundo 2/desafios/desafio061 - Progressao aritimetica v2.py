'''
Refaça o DESAFIO051, lendo o primeiro termo de uma PA, mostrando os 10 primeiros termos
da progressao usando a estrutura WHILE sem utilizar a formula da PA'''

#Minha resposta
print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = t1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

