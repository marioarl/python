'''Faca um programa que leia nome e média de um aluno, guardando também a situacao (se 7 ou mais aprovado)
em um dicionario. No final mostre o conteudo da estrutura na tela.'''

# minha resposta
boletim = dict()
boletim['nome'] = str(input('Nome: ')).strip()
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim["media"] >= 7:
    boletim["situacao"] = 'Aprovado'
if 7 > boletim["media"] >= 5:
    boletim["situacao"] = 'Recuperacao'
if boletim["media"] < 5:
    boletim["situacao"] = 'Reprovado'
print(f'O nome é igual a {boletim["nome"]}')
print(f'Média igual a {boletim["media"]} ')
print(f'A situacao é igual a {boletim["situacao"]}')

#resposta Gustavo
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >=7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')



