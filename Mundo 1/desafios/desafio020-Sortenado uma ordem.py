'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
'''

#minha resposta
'''import random
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
lista = [a1, a2, a3, a4]
ordem = random.shuffle(lista) #não há necessidade de criar outro variavel(ordem)
print('A ordem de apresentação será')
print (lista)'''

#resposta do Gustavo
import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print (lista)