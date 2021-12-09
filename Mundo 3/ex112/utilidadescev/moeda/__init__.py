def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, perc=0, formato=False):
    res = n + (n * (perc/100))
    return res if formato is False else moeda(res)


def diminuir(n=0, perc=0, formato=False):
    res = n - (n * (perc/100))
    return res if formato is False else moeda(res)


def moeda(n=0, moeda ='R$ '):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n=0, b=10, c=5):
    dic = {'Preço analisado:': moeda(n), 'Dobro do preço:': dobro(n, True),
           'Metade do preço:': metade(n, True), f'{b}% de aumento:': aumentar(n, b, True),
           f'{c}% de redução:': diminuir(n, c, True)}
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    for k, v in dic.items():
        print(f'{k:<20} {v:<5}')
    print('-' * 30)
