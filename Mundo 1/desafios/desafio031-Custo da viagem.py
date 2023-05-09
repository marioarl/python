'''
Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
para viagens mais longas.
'''

#minha resposta
#dist = float(input('Qual a distancia da sua viagem? '))
#print('Voce está prestes a começar uma viagem de {:.1f}Km'.format(dist))
#if dist <= 200:
#    print('E o preço da sua passagem será de R${:.2f}'.format(dist * 0.50))
#else:
#    print('E o preço da sua passagem será de R${:.2f}'.format(dist * 0.45))

#resposta1 do Gustavo
#distancia = float(input('Qual a distancia da sua viagem? '))
#print('Voce está prestes a começar uma viagem de {:.1f}Km'.format(distancia))
#if distancia <= 200:
#    preco = distancia * 0.50
#else:
#    preco = distancia * 0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(preco))

#resposta2 do gustavo
distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce está prestes a começar uma viagem de {:.1f}Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 #if in line ou operador ternario
print('E o preço da sua passagem será de R${:.2f}'.format(preco))