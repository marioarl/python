#Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50

#Minha resposta
for par in range(2, 51, 2):
    print(par, end=' ') #o comando end=' ' coloca as linhas horizontais em verticais
print('Acabou')

#Resposta1 do Gustavo
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')

#resposta2 do Gustavo
#for n in range(2, 51, 2):
#    print(n, end=' ')
#print('Acabou')
