'''
Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex. Digite um numero: 1834
 unidade: 4
 dezena: 3
 centena: 8
 milhar: 1
 '''

#minha resposta
numero = str(input('Digite um numero inteiro: ')).strip()
lista_num = list(numero)
if int(numero) >=0 and int(numero) <=9:
    print(f'Unidade.: {lista_num[0]}')
    print(f'Dezena..: 0')
    print(f'Centena.: 0')
    print(f'Milhar..: 0')
elif int(numero) >=10 and int(numero) <=99:
    print(f'Unidade.: {lista_num[1]}')
    print(f'Dezena..: {lista_num[0]}')
    print(f'Centena.: 0')
    print(f'Milhar..: 0')
elif int(numero) >=100 and int(numero) <=999:
    print(f'Unidade.: {lista_num[2]}')
    print(f'Dezena..: {lista_num[1]}')
    print(f'Centena.: {lista_num[0]}')
    print(f'Milhar..: 0')
elif int(numero) >=1000 and int(numero) <=9999:
    print(f'Unidade.: {lista_num[3]}')
    print(f'Dezena..: {lista_num[2]}')
    print(f'Centena.: {lista_num[1]}')
    print(f'Milhar..: {lista_num[0]}')
else:
    print(f'Numero {numero} está fora do escopo do programa, tente um numero de 0 até 9999')

#resposta do Gustavo
num = int(input('Informe o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))