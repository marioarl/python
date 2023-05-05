""""
Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possiveis sobre ela
"""

#minha resposta
frase = str(input("Digite algo: "))
print(f"O tipo primitivo desse valor é {type(frase)}")
print(f"Só tem espaços? ", frase.isspace())
print(f"É um numero? ", frase.isnumeric())
print(f"É alfabetico? ", frase.isalpha())
print(f"É alfanumerico? ", frase.isalnum())
print(f"Está em maiusculas? ", frase.isupper())
print(f"Está em minusculas? ", frase.islower())
print(f"Está capitalizada? ", frase.istitle())




#Resposta do Gustavo
'''a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiusculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())'''

