'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condicao de pagamento:
 - á vista dinheiro/cheque: 10% de desconto
 - á vista no cartao: 5% de desconto
 - em até 2x no cartao: preço normal
 - 3x ou mais no cartao: 20% de juros
 '''

#Minha resposta
print('='*10, 'LOJAS GUANABARA', '='*10)
compra = float(input('Preço das compras: R$ '))
print ('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão'
       '\n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, compra - (compra * 10 / 100)))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(compra, compra - (compra * 5 / 100)))
elif opcao == 3:
    print('Sua compra será parcelada em 2X de R${:.2f} SEM JUROS'.format(compra / 2))
if opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    ncompra = compra + (compra * 20 / 100)
    print('Sua compra será parcelada em \033[7;33m{}X\033[m de \033[7;33mR${:.2f}\033[m \033[1;31mCOM JUROS\033[m'.format(parcela, ncompra / parcela ))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, ncompra))
else:
    print('\033[7;31mOPCAO INVÁLIDA.\033[m Tente novamente')

#Resposta Gustavo
print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2X de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('OPCÃO INVALIDA de pagamento. Tente novamente ')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
