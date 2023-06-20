'''
Crie um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10
primeiros termos dessa progressao.
'''

#Minha resposta
print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
an = termo + (10 -1) * razao #formula da PA
for m in range(termo, an + 1 , razao):
    print('{} ->'.format(m), end=' ')
print('ACABOU')

#Resposta gustavo
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end = '-> ')
print('ACABOU')



