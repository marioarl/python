nome = str(input('Qual é o seu nome? ')).strip().upper()
if nome == 'MARIO':
    print('Mas que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'JOAO':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))