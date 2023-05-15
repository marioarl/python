'''
Desenvolva um programa que leia o comprimento e tres retas e diga ao usuario se elas
podem ou nao formar um triangulo
'''

#minha resposta
print('-='*20)
print('Analisador de Trinagulos')
print('-='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2: #condicao de existencia do triangulo
    print('Os segmentos acima PODEM FORMAR triangulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo')

#Resposta do Guanabara
print('='*20)
print('Analisador de Triangulos')
print('='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo!')