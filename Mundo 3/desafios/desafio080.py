#crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma
#lista, já na posicao correta de insercao(sem usar o SORT())
#No final, mostre a lista ordenada na tela

#resposta do Gustavo
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')