'''
Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor
digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo
'''

#minha resposta
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*30)
    print(f'''{num} x 1 = {num*1}
{num} x 2 = {num*2}
{num} x 3 = {num*3}
{num} x 4 = {num*4}
{num} x 5 = {num*5}
{num} x 6 = {num*6}
{num} x 7 = {num*7}
{num} x 8 = {num*8}
{num} x 9 = {num*9}
{num} x 10 = {num*10}''')
    print('-'*30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

#Resposta do Gustavo
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')