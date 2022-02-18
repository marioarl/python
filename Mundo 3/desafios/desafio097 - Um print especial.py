#crie um programa que tenha a funcao chamada escreva(), que receba um texto qualquer como parametro e mostre
# uma mensagem com tamanho adaptavel.
#Ex. escreva('Ola Mundo!')
# Saida  ˜˜˜˜˜˜˜˜˜˜
#        Olá Mundo!
#        ˜˜˜˜˜˜˜˜˜

#minha resposta
def escreva(msg):
    print('~' * (len(msg) + 4))  # pra ficar com 2 ~ na esquerda e 2 ~ na direita sobrando
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


#programa principal
escreva('Mario Lima')
escreva('Lactobacilos vivos')
escreva('Oi')

#resposta do Gustavo
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)  # pra ficar com 2 ~ na esquerda e 2 ~ na direita sobrando
    print(f'  {msg}')
    print('~' * tam)


#programa principal
escreva('Gustavo Guanabara')
escreva('Curso em Python no YouTube')
escreva('CeV')
