#crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o
#programa deverá perguntar se o usuario quer ou nao continuar. No final mostre:
#A) quantas pessoas tem mais de 18 anos
#B) quantos homens foram cadastrados
#C) quantas mulheres tem menos de 20 anos.
#minha resposta
mais18 = h = m = menos20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        h += 1
    elif sexo == 'F' and idade < 20:
        m += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            h += 1
        elif sexo == 'F' and idade < 20:
            m += 1
    print('-'*20)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('='*6, 'FIM DO PROGRAMA', '='*6)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')

#resposta do Gustavo
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

