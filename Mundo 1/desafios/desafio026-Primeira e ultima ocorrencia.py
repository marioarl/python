'''Faça um programa que leia uma frase pelo teclado e mostre:
 * Quantas vezes aparece a letra "A"
 * Em que posição ela aparece a primeira vez
 * Em que posição ela aparece a ultima vez'''

#minha resposta
#frase = str(input('Digite uma frase: ')).strip()
#mfrase = frase.lower()
#print('A letra A aparece {} vezes na frase'.format(mfrase.count('a')))
#print('A primeira letra A apareceu na posição {}'.format(mfrase.find('a')))
#print('A ultima letra A apareceu na posição {}'.format(mfrase.find('a'))) #nao consegui fazer a posicao final

#resposta do Gustavo
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))