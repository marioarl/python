#Exemplo 1
#nome = str(input('Qual o seu nome? '))
#if nome == 'Gustavo':
#    print('Que nome lindo voce tem!')
#else:
#    print('Seu nome é tao normal!')
#print('Bom dia {}!'.format(nome))

#Exemplo2
#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1 + n2) / 2
#print('A sua média foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('Sua média foi boa! PARABENS!')
#else:
#    print('Sua média foi ruim! ESTUDE MAIS!')

#Exemplo 3
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABENS'if m >=6.0 else 'ESTUDE MAIS!') #Condicao simplificada