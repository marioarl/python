'''
Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do prg mostre:
 A media de idade do grupo
 Qual é o nome do homem mais velho
 Quantas mulheres tem menos de 21 anos
 
 '''

#Minha resposta
somaIdade = homemMaisVelho = mulherMenos20 = 0
nomeMaisVelho = ""
for p in range(1,5):
    print(f"---- {p}a. PESSOA ----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    somaIdade += idade
    if sexo in "M" and p ==1:
        homemMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in "M" and idade > homemMaisVelho:
        homemMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in "F" and idade < 20:
        mulherMenos20 += 1
media = somaIdade / 4
print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {homemMaisVelho} anos e se chama {nomeMaisVelho}")
print(f"Ao todo são {mulherMenos20} mulheres com menos de 20 anos")

#Resposta Gustavo
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1,5):
    print("----- {}a. PESSOA -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("A media de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
