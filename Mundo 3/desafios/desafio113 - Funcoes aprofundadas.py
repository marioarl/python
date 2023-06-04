'''
Reescreva a funcao leiaint() que fizemos no desafio104, incluindo agora a possibilidade da digitacao
de um numero de tipo invalido. Aproveite e crie uma funcao leiafloat() com a mesma funcionalidade
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


#Programa principal
n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

