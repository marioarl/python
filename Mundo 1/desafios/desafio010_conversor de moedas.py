'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$ 1,00 = R$ 3,27'''

#Minha resposta
print ('='*50)
print('CONVERSOR DE MOEDA')
print('='*50)
dinheiro = float(input ('| Quanto dinheiro voce tem na carteira? R$ '))
print ('|')
print('| Com R${:.2f} voce pode comprar US${:.2f}!'.format(dinheiro, dinheiro / 3.27))
print('='*50)

#minha resposta melhorada
print ('='*50)
print('|', '\033[1;7;34m                CONVERSOR DE MOEDA            \033[m |')
print('='*50)
moeda = str(input('\033[1;35mVoce quer converter qual moeda?\033[m ')).strip().upper()
conv = str(input('\033[1;36mPara qual moeda voce quer converter?\033[m ')).strip().upper()
if moeda == 'REAL' and conv == 'DOLAR':
    d = float(input('\nQuanto dinheiro voce tem? R$ '))
    print('Com R$ {:.2f} voce pode comprar US$ {:.2f}'.format(d, d / 5.41))
if moeda == 'DOLAR' and conv == 'REAL':
    d = float(input('\nQuanto dinheiro voce tem? US$ '))
    print('Com US${:.2f} voce pode comprar R${:.2f}'.format(d, d * 5.41))
if moeda == 'REAL' and conv == 'EURO':
    d = float(input('\nQuanto dinheiro voce tem? R$ '))
    print('Com R$ {:.2f} voce pode comprar € {:.2f}'.format(d, d / 6.52))
if moeda == 'EURO' and conv == 'REAL':
    d = float(input('\nQuanto dinheiro voce tem? € '))
    print('Com € {:.2f} voce pode comprar R$ {:.2f}'.format(d, d * 6.52))
if moeda == 'DOLAR' and conv == 'EURO':
    d = float(input('\nQuanto dinheiro voce tem? US$ '))
    print('Com US$ {:.2f} voce pode comprar € {:.2f}'.format(d, d * 0.83))
if moeda == 'EURO' and conv == 'DOLAR':
    d = float(input('\nQuanto dinheiro voce tem? € '))
    print('Com € {:.2f} voce pode comprar US$ {:.2f}'. format(d, d / 0.83))


#resposta do Gustavo
#real = float(input('Quanto dinheiro voce tem na carteira? R$ '))
#dolar = real / 3.27
#print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))

