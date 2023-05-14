#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto

#Minha resposta - nao consegui esta dando erro
from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
print(f"O ano {ano} ", end="")
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"é BISSEXTO")
else:
    print(f"não é BISSEXTO")

#resposta do Gustavo
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year #esta instrucao vai pegar o ano atual configurado na maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
