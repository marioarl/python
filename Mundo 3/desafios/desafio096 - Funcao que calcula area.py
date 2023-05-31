'''
Crie um programa que tenha uma funcao chamada area(), que receba as dimensoes de um terreno retangular
(largura e comprimento) e mostre a area do terreno
'''

#minha resposta
#def area(larg, c):
#    a = larg * c
#    print(f'A area de um terreno {larg}x{c} é de {a}m2.')

#Programa Principal
#print('Controle de Terernos')
#print('-'*20)
#larg = float(input('LARGURA (m): '))
#c = float(input('COMPRIMENTO (m): '))
#area(larg, c)


#resposta do Gustavo
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m2.')


#Programa principal
print('Controle de Terrenos')
print('-' * 20)
l= float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m) '))
area(l, c)

