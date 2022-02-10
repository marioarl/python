#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte
#ao usuario qual será o valor a ser sacado(numero inteiro) e o programa vai informar quantas
#cedulas de cada valor serao entregues.
#OBS: Considere que o caixa possui cedulas de R$50 R$20 R$10 e R$1
from time import sleep
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Contando {totced} cedulas de R${ced}...')
            sleep(1)
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(f'{"O Dinheiro está saindo no local indicado..."}'.upper())
sleep(1)
print(f'Obrigado por utilizar o BANCO TABAJARA')

