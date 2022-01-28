#faça um programa que leia um ano qualquer e mostre se ele é Bissexto

#minha resposta - nao consegui esta dando erro
#ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
#bissexto = ano % 4
#bissexto2 = ano % 100
#bissexto3 = ano % 400
#total = bissexto + bissexto2 + bissexto3
#if total == 0:
#    print('O ano {} é BISSEXTO'.format(ano))
#else:
#    print('O ano {} NÃO é BISSEXTO'.format(ano))

#resposta do Gustavo
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year #esta instrucao vai pegar o ano atual configurado na maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
