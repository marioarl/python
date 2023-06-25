'''
Crie uma TUPLA preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de
futebol, na ordem de colocacao. Depois mostre:
A) apenas os 5 primeiros colocados
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica
D) Em que posicao na tabela está o time da Chapecoense
'''

#Minha resposta
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
chap = times.index('Chapecoense') + 1
print('-='*30)
print(f'\033[35mLista de times do Brasileirao:\033[m {times}')
print('-='*30)
print(f'\033[36mOs 5 primeiros sao:\033[m {times[0:5]}')
print('-='*30)
print(f'\033[33mOs 4 ultimos sao:\033[m {times[16:20]}')
print('-='*30)
print('\033[32mTimes em ordem alfabetica:\033[m',sorted(times))
print('-='*30)
print(f'\033[31mO Chapecoense está na {chap}a. posicao\033[m')

#Reposta do Gustavo
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
print('-='*15)
print(f'Lista de times do Brasileirao: {times}')
print('-='*15)
print(f'Os 5 primeiros sao:\033[m {times[0:5]}')
print('-='*15)
print(f'Os 4 ultimos sao: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}a. posicao')# Aqui foi utilizado o " para identificar a string que será veiricada pelo index, pois o Python nao aceita ' dentro de outra '

