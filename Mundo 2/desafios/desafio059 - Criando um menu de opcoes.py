'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ]somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos numeros
[ 5 ]sair do programa
seu programa devera realizar a opercao solicitada em cada caso.
'''

#Minha resposta
from time import sleep
print('\033[36m=-=\033[m'*20)
print('\033[7;33m{:^80}'.format('PROGRAMA DE CALCULOS                     \033[m'))
print('\033[36m=-=\033[m'*20)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    sleep(0.5)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('\033[7;34m>>>>> Qual é sua opção?\033[m '))
    sleep(0.25)
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    if opcao == 2:
        mult = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, mult))
    if opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            print('Os numeros {} e {} são iguais!'.format(n1, n2))
    if opcao == 4:
        print('Inform os numeros novamente:')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    print('\033[36m=-=\033[m'*20)
    if opcao > 5:
        print('\033[31mOpção inválida, tente novamente!!!\033[m')
print('Finalizando...')
sleep(0.5)
print('Obrigado por usar o programa!!!')

#resposta do Gustavo
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0
while opcao != 5:
    print('''      [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa! Volte sempre!')