#crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
#ainda nao atingiram a maioridade e quantas ja sao maiores.
"""minha resposta
from datetime import date
maior = menor = 0
for a in range(1,8):
    nasc = int(input(f"Em que ano a {a}a. pessoa nasceu? "))
    idade = date.today().year - nasc
    if idade >=21:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"E tambem tivemos {menor} pessoas menores de idade")
"""

#resposta Gustavo
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}a. pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))
