#Faça um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem
#pares. Se o valor digitado form impar, desconsidere-o

#minha resposta ( igual a do Gustavo)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voce informou {} numeros PARES e a soma foi {}'.format(cont, soma))