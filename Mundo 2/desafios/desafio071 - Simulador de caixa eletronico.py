'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte
ao usuario qual será o valor a ser sacado(numero inteiro) e o programa vai informar quantas
cedulas de cada valor serao entregues.
OBS: Considere que o caixa possui cedulas de R$50 R$20 R$10 e R$1'''

#Minha resposta
print("="*40)
print("BANCO ASPA".center(40))
print("="*40)
valor = float(input("Qual o valor voce quer sacar? R$"))

total = valor
cedulas = 50
total_cedulas = 0

while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Contando {total_cedulas} cedulas de R${cedulas}...')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0

        if total == 0:
            break
print('='*40)
print('FIM DA OPERAÇÃO') 

#Resposta do Gustavo
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Contando {totced} cedulas de R${ced}...')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre a BANCO CEV! Tenha um bom dia!')

