'''Faça um prg que tenha uma funcao chamada contador(), que receba 3 parametros: inicio, fim e passo e realize
a contagem. Seu programa tem que realizar 3 contagens atraves da funcao criada:
a) de 1 ate 10. de 1 em 1  b) de 10 até 0, de 2 em 2   c) uma contagem peersonalizada'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -=p
        print('FIM!')


#programa principal
contador(0, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

