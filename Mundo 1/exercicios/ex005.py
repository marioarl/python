# importando a biblioteca math inteira
#import math
#num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
#print ('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz))) # math.ceil arredondar para cima

#importando somente a funcao sqrt da biblioteca math
#from math import sqrt
#num = int(input('Digite um numero: '))
#raiz = sqrt(num)
#print('A raiz quadrada de {} é igual a {}'.format(num, raiz))

#importando somente as funcoes sqrt e floor da biblioteca math
#from math import sqrt, floor
#num = int(input('Digite um numero: '))
#raiz = sqrt(num)
#print('A raiz quadrada de {} é igual a {:.2f}'.format(num, floor(raiz)))

#importanto a biblioteca random, que o computador gera um numero aleatorio entre 0 e 1
# o metodo random da biblioteca random ele gera um numero aleatorio entre 0 e 1
#import random
#num = random.random()
#print(num)

# utilizando o metodo randint da biblioteca random ele gera um numero aleatorio entre 0 e 1
import random
num1 = random.randint(1, 60)
num2 = random.randint(1, 60)
num3 = random.randint(1, 60)
num4 = random.randint(1, 60)
num5 = random.randint(1, 60)
num6 = random.randint(1, 60)
print(num1, num2, num3, num4, num5, num6)