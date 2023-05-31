'''
Aprimore o desafio093 para que ele funcione com varios jogadores, incluindo um sistema de visualizacao
de detalhes do aproveitamento de cada jogador.
'''
#Minha Resposta
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-'*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador com código {mostrar}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"]}')
        for i, g in enumerate(time[mostrar]['gols']):
            print(f'   No jogo {i+1} fez {g}gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

#Resposta do Gustavo
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-'*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador com código {mostrar}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"]}')
        for i, g in enumerate(time[mostrar]['gols']):
            print(f'   No jogo {i+1} fez {g}gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

