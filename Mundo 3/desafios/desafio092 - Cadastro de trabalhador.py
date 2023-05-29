'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalhoe cadastre-os (com idade) em um
dicionario se por acaso a CTPS for diferente de zero, o dicionario receberá tambem o ano de contratacao e o salario
Calclue e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
'''

#minha resposta
from datetime import date
atual = date.today().year
lista = dict()
lista['nome'] = str(input('Nome: ').strip())
ano = int(input('Ano de nascimento: '))
lista['idade'] = atual - ano
lista['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if lista['ctps'] != 0:
    lista['contratacao'] = int(input('Ano de contratacao: '))
    lista['salario'] = float(input('Salario: '))
    lista['aposentadoria'] = (lista['contratacao'] + 35) - ano
print('-='*40)
print(lista)
for k, i in lista.items():
    print(f'{k} tem o valor {i}')

#resposta do Gustavo igual
hoje = date.today().year
ficha = dict()
ficha['nome'] = str(input('Nome: ').strip())
ano = int(input('Ano de nascimento: '))
ficha['idade'] = hoje - ano
ficha['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratacao'] = int(input('Ano de contratacao: '))
    ficha['salario'] = float(input('Salario: '))
    ficha['aposentadoria'] = (ficha['contratacao'] + 35) - ano
print('-='*40)
print(ficha)
for k, i in ficha.items():
    print(f'{k} tem o valor {i}')