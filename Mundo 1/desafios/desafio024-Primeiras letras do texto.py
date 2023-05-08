'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com nome de "Santo"
'''

#minha resposta
cidade = str(input('Em que cidade voce nasceu? ')).strip()
print(cidade)
print(cidade[:5].upper() == 'SANTO')

#resposta do Gustavo
#cid = str(input('Em que cidade voce nasceu?')).strip()
#print(cid[:5].upper() == 'SANTO')