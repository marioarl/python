#crie um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres
# e que se encontram no intervalo de 1 até 500


#minha resposta (nao consegui fazer)
#for imp in range(1, 10, 2):
#    if imp % 3 == 0:
#        print(imp)


#respotsa Gustavo
#soma = 0 # acumulador
#cont = 0 # acumulador
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        soma = soma + c # pode-se usar a forma simplificada soma += c
#        cont = cont + 1 # pode-se usar a forma simplificada cont += 1
#print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

#minha outra resposta
soma = 0
cont = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))




