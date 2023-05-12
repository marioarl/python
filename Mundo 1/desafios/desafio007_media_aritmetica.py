# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

#minha resposta
print('\033[1;34m#'*20, '\033[7;33mMÉDIA DO ALUNO\033[m', '\033[1;34m#\033[m'*20)
n1 = float(input('\n\033[1;35mPrimeira nota do aluno:\033[m '))
n2 = float(input('\n\033[1;33mSegunda nota do aluno:\033[m '))
print('\033[1;36mA média entre\033[m \033[1;35m{}\033[m e \033[1;33m{}\033[m é igual a \033[1;7;32m{:.2f}\033[m'.format (n1, n2, (n1+n2)/2))

#resposta do Gustavo
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2)/2
print('A média entre {} e {} é igual a {:.2f}'.format(n1, n2, media))