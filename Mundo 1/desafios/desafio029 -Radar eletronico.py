'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite'''

#minha resposta
#velo = float(input('Qual é a velocidade do carro? '))
#multa = (velo - 80) * 7.0
#if velo <= 80:
#    print('Tenha um bom dia! Dirija com segurança!')
#else:
#    print('MULTADO! Voce excedeu o limite que é de 80Km/h')
#    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
#    print('Tenha um bom dia! Dirija com segurança!')

#resposta do Gustavo
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')