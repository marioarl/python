'''
Crie um prg que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
A)Quantas pessoas foram cadastradas
B)A média de idade do grupo
C)Uma lista com todas as mulheres.
D)Uma lista com todas as pessoas com idade acima da média'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ').strip())
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ').strip().upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ', end='')
print()
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')


