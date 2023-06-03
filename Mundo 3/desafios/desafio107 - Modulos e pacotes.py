'''
Crie um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminuir, dobro(), metade()
Faca tambem um programa que importe esse modulo e use algumas dessas funcoes'''

from ex107 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')