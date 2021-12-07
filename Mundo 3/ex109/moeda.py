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

