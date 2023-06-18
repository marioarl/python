'''
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa
vai perguntar o valor da casa , o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao
o emprestimo será negado
'''

#Minha resposta
casav = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prest = casav / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casav, anos, prest))
if prest <= (salario * 30 / 100):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

#Resposta do Gustavo
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos a prestacao será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
