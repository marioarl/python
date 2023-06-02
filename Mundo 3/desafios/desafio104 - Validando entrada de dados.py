'''Crie um programa que tenha a funçao leiaint(), que vai funcionar de forma semelhante a funcao input(),só que fazendo a validacao para aceitar apenas um valor numerico.'''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero valido.\033[m')
        if ok:
            break
    return valor


# programa principal
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
