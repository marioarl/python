'''crie um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 até 500'''


#Minha resposta
cont = soma = 0
for i in range(1,500,2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma de todos os {cont} valores solicitados é {soma}')

#Respotsa Gustavo
soma = 0 # acumulador
cont = 0 # acumulador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c # pode-se usar a forma simplificada soma += c
        cont = cont + 1 # pode-se usar a forma simplificada cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))





