'''
Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitacao novamente até ter um valor correto
'''

#minha resposta
#sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
#while sexo != 'M' and sexo != 'F':
#    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()
#print('Sexo {} registrado com sucesso'.format(sexo))

#resposta do Gustavo
sexo = str(input('Informe seu sexo: [M,F]')).strip().upper()[0] #o [0] significa se escrever Masculino ou Feminino, pegará somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(sexo))
