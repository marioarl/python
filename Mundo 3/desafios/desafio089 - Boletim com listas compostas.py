'''crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final
mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno
individualmente'''
ficha = list ()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'{"No.":>1}', f'{"NOME":<15}', f'{"MÉDIA"}')
print('-'*30)
for i, c in enumerate(ficha):
    print(f'{i:<3} {c[0]:<15} {c[2]:.1f}')
while True:
    print('-'*30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(ficha) - 1:
        print(f'A nota do aluno {ficha[mostrar][0]} são {ficha[mostrar][1]}')
print('<<< VOLTE SEMPRE >>>')
