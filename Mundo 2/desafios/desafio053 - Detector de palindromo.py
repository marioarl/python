'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindrono, desconsiderando
os espaçoes  EX: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

#Minha resposta
frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
contrario = ''
for c in range(len(all) - 1, -1, -1):
    contrario += junto[c]
print('O invesro de {} é {}'.format(junto, contrario))
if contrario == junto:
    print('Temos um palindomo!')
else:
    print('A frase digitada não é um palindromo')

#Resposta1 do Gustavo
frase = str(input('Digite uma frase: ')).strip().upper()
div = frase.split()
all = ''.join(div)
inverso = ''
for c in range(len(all) - 1, -1, -1):
    inverso += all[c]
print('O invesro de {} é {}'.format(all, inverso))
if inverso == all:
    print('Temos um palindomo!')
else:
    print('A frase digitada não é um palindromo')

#resposta2 do Gustavo
frase = str(input('Digite uma frase: ')).strip().upper()
div = frase.split()
all = ''.join(div)
inverso = all[::-1]
print('O invesro de {} é {}'.format(all, inverso))
if inverso == all:
    print('Temos um palindomo!')
else:
    print('A frase digitada não é um palindromo')

