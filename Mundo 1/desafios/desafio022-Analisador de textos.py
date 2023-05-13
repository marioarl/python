'''Crie um programa que leia o nome completo da pessoa e mostre:
* O nome com todas as letras maiusculas
* o nome com todas as letras minusculas
* Quantas letras ao tem o nome (sem considerar o espaco)
* Quantas letras tem o primeiro nome'''

#Minha resposta
nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format (nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo', len(nome), 'letras') #nao consigo tirar os espacos em branco
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))

#Resposta 1 do Gustavo
nome = str(input('Digite seu nome completo: ')).strip() #strip retira os espacos do inicio e do fim
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#resposta 2 do Gustavo
nome = str(input('Digite seu nome completo: ')).strip() #strip retira os espacos do inicio e do fim
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))