#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

#minha resposta
print('\033[1;36m+=\033[m'*15, '\033[1;7;36mPRODUTO COM DESCONTO\033[m', '\033[1;36m+=\033[m'*15)
produto = float(input ('\033[31mQual o preço do produto? R$\033[m'))
calculo = produto * 0.05 #5% do valor
desconto = produto - calculo
print ('\033[33mO produto que custava \033[1;7;33mR${:.2f}\033[m, \033[33mna promoção com desconto de \033[m\033[1;7;33m5%\033[m \033[33mvai custar \033[1;7;33mR${:.2f}\033[m'.format(produto, desconto))

#resposta do Gustavo
#preco = float(input('Qual o preço do produto? R$'))
#novo = preco - (preco * 5 / 100)
#print ('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))