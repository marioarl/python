'''Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
no final, de acordo com a media atingida:
 - media abaixo de 5.0: REPROVADO
 - media entre 5.0 e 6.9 RECUPERACAO
 - média 7.0 ou superior APROVADO'''

#minha resposta
#nt1 = float(input('Primeira nota: '))
#nt2 = float(input('Segunda nota: '))
#media = (nt1 + nt2) / 2
#print('Tirando {} e {} a média do aluno é {:.1f}'.format(nt1, nt2, media))
#if media >= 7.0:
#    print('O aluno está APROVADO!')
#elif media < 7.0 and media >= 5.0:
#    print('O aluno está de RECUPERAÇÃO!')
#elif media < 5.0:
#    print('O aluno está REPROVADO!')

#resposta Gustavo
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >=5:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print('O aluno está REPROVADO')
elif media >=7:
    print('O aluno está APROVADO')
