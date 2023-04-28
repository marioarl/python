#crie um programa que tenha uma TUPLA com varias palavras (nao usar acento). Depois disso, voce
#deve mostrar, para cada palavra, quais sao as suas vogais

#minha resposta




#resposta do Gustavo
palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
