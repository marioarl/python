#crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do prg mostre:
# A media de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 21 anos
somaidade = velho = mulherid = 0
nvelho = ' '
for c in range(1, 5):
    print('-'*6, '{}a. PESSOA'.format(c), '-'*6)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1:
        velho = idade
        nvelho = nome
    else:
        if idade > velho:
            velho = idade
            nvelho = nome
    if sexo == 'F':
        if idade < 20:
            mulherid += 1

print('A média de idade do grupo é de {:.1f} anos'.format(somaidade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulherid))
