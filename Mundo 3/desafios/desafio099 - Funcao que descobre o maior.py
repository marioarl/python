'''
Crie um prg que tenha a funcao chamada maio(), que receba varios parametros com valores inteiros. Seu
programa tem que analisar todos os valores e dizer qual deles é o maior
'''
#minha resposta
#from time import sleep


#def maior(*num):
#    n = [num]
#    print('-='*30)
#    print('Analisando os valores passados...')
#    for c in num:
#        print(f'{c} ', end='')
#        sleep(0.5)
#    print(f'Foram informados {len(num)} valores ao todo.')
#    print('O maior valor informado foi', max(num))


#programa principal
#maior(2, 9, 4, 5, 7, 1)
#maior(4, 7, 0)
#maior(1, 2)
#maior(6)
#maior(0)

#resposta do Gustavo
from time import sleep


def maior(*num):
    cont = maior = 0
    print('-='* 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
