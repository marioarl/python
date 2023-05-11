'''
A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SENIOR
Acima : MASTER
'''

#minha resposta
#from datetime import date
#ano = int(input('Ano de nascimento: '))
#atual = date.today().year
#idade = atual - ano
#print('O atleta tem {} anos'.format(idade))
#if idade <= 9:
#    print('Classificação: MIRIM')
#elif idade > 9 and idade <= 14:
#    print('Classificação: INFANTIL')
#elif idade > 14 and idade <= 19:
#    print('Classificacao: JUNIOR')
#elif idade >19 and idade <= 25:
#    print('Classificação: SENIOR')
#elif idade > 25:
#    print('Classificação: MASTER')

#resposta do Gustavo
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNOIR')
elif idade <=25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

