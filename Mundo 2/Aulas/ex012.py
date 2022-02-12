for c in range(0, 6):
    print('Oi')
print('FIM')

for c in range(0, 6):
    print(c)
print('FIM')

for c in range(6, 0, -1): #contou de 6 até 1
    print(c)
print('FIM')

for c in range(0, 7, 2): #contou de 0 até 7 de dois em dois
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0, n+1): #conta até o numero que voce digitou
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3): #irá imprimir 3 x o comando  digite um valor
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n #ou s += n
print('A somatoria de todos os valores foi {}'.format(s))
