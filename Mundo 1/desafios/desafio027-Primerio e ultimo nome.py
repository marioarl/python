#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
# separadamente.
#Ex. Ana Maria de Souza
# primeiro = Ana     segundo = Souza

#minha resposta
#nome = str(input('Digite seu nome completo: ')).strip().split()
#ultimo = (len(nome) - 1)
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu ultimo nome é {}'.format(nome[ultimo]))

#resposta do Gustavo
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))