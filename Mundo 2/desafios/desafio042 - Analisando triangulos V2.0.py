'''
Refaça o DESAFIO035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo
acrescentando o recurso de mostrar que tipo de trinagulo será formado:
Equilatero: todos os lados iguais
isoceles: dois lados iguais
Escaleno: todos os lados diferentes
'''

#minha resposta
#r1 = float(input('Primeiro segmento: '))
#r2 = float(input('Segundo segmento: '))
#r3 = float(input('Terceiro segmento: '))
#if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
#    if r1 == r2 == r3:
#        tipo = 'EQUILATERO'
#    elif r1 == r2 or r2 == r3 or r1 == r3:
#        tipo = 'ISOCELES'
#    elif r1 !=r2 or r2 != r3 or r1 != r3:
#        tipo = 'ESCALENO'
#    print('Os segmentos acima PODEM FORMAR um triangulo {}'.format(tipo))
#else:
#    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')

#resposta Gustavo
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end= '')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')