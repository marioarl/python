pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # Neste caso se usar aspas simples na declaracao de pessoas, dará erro, tem
                                        # que usar aspas DUPLAS
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
#del pessoas['sexo']
print()
pessoas ['nome'] = 'Leandro' #modificar o dicionario
pessoas['peso'] = 98.5 #acrescentar elementos
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*50)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print('-='*50)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # copiar o dicionario, como em lista que usamos [:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v    }')