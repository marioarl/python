'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado
'''

#Minha resposta
dias1 = int(input('Quantos dias alugados? '))
km1 = int(input('Quantos Km rodados? '))
pdia = dias1 * 60
pkm = km1 * 0.15
total = pdia + pkm
print('O total a pagar é de R${:.2f}'.format(total))

#resposta do Gustavo
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
