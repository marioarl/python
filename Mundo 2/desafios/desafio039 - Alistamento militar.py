#faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao servico militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento.
#Seu programa tambem deverá mostrar o tempo que falta ou que passou o prazo

#minha resposta
#from datetime import date
#nasc = int(input('Ano de nascimento: '))
#data = date.today().year
#idade = data - nasc
#anos = 18 - idade
#print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, data))
#if idade < 18:
#    print('Ainda faltam {} anos para o alistamento'.format(anos))
#    print('Seu alisatamento será em {}'.format(data + anos))
#elif idade > 18:
#    print('Voce deveria ter se alistado há {} anos'.format(idade - 18))
#    print('Seu alistamento foi em {}'.format(nasc + 18))
#elif idade == 18:
#    (print('Voce tem que se alistar IMEDIATAMENTE!!!'))

#resposta do Gustavo
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

