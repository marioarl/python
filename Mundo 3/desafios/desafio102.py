#Crie um programa que tenha a funcao fatorial() que receba dois parametros: o primeiro que indique o
#numero a calcular e o outro chamado show, que será uma valor logico(opcional) indicando se será mostrado
#ou nao na tela o processo de calculo do fatorial

def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta do fatorial
    :return: O valor do fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#programa principal
print(fatorial(20, True))
