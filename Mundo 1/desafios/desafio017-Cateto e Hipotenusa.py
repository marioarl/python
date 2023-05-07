'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triangulo retangulo, calcule e mostre o comprimento da hipotenusa'''

#minha resposta 1
''''import math
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hyp = math.hypot(cato, cata)
print ('A hipotenusa vai medir {:.2f}'.format(hyp))
'''
#minha resposta 2
'''from math import hypot
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hyp = hypot(cato, cata)
print('A hipotenusa vai medir {:.2f}'.format(hyp))'''

#minha resposta 3, sem importar a biblioteca math
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format((cato*cato + cata*cata)**(1/2)))

#resposta 1 do Gustavo, sem importar a biblioteca math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hi))

#resposta 2 do Gustavo, importanto a biblioteca math
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
num = 1.3
print(math.sqrt(81))
print(num)