#Faca um programa que tenha função chamada ficha(), que receba dois parametros opcionais> o nome do jogador
# e quantos gols marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha
#sido informado corretamente.
def ficha(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')

#programa principal
print('-' * 30)
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(b=gols)
else:
    ficha(nome, gols)
