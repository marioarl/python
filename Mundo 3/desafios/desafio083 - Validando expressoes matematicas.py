#crie um programa onde o usuario digite uma expressao matematica qualquer que use parenteses.
#Seu programa devera analisar se a expressao passada esta com os parenteses abertos e fechados
#na ordem correta

#resposta do Gustavo
expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(')')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            break
if len(pilha) == 0:
    print('Sua expressao está valida!')
else:
    print('Sua expressao está errada!')
print(pilha)
