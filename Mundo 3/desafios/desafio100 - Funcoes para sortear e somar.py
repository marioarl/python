'''Crie um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e somaPar(). A primeira funcao vai sortear 5 numeros e vai coloca-los dentro de uma lista e a segunda funcao vai mostrar a soma entre todos os valores PARES sorteados pela funcao anterior.'''
from random import randint
from time import sleep


def sorteia(lista): #2a. criar a funcao sorteia() , 5a. a funcao sorteia recebe lista como parametro
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5): #6o. cria for para escolher os numeros
        n = randint(1, 10)  # 7o. variavel n recebe randint de 1 ate 10
        lista.append(n) #8o. colocar na lista os numeros sorteados da variavel n
        print(f'{n} ', end='') #9o. imprimir os valores sorteados
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista): #3a. criar a funcao somaPar() recebendo a lista e coloca-la como comentario
    soma = 0 #11o. criar uma variavel com 0
    for valor in lista: #12o. for para verificar se o numero é PAR
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valore PARES de {lista}, temos {soma}')#13o. Mostrar a lista e a soma dos PARES



#Programa Principal
numeros = list() #1a. criar uma lista vazia de numeros
sorteia(numeros) #4a. chamar a funcao sorteia
somaPar(numeros) #10o. chamar a funcao somaPar