#quando voce sabe o limite
#for c in range(1, 10):
#    print(c)
#print('FIM')

#c = 1 #este contador se refere ao range do comando for range(1, 10)
#while c < 10: # este  < 10 se refere ao range do comando for range(1, 10)
#    print(c)
#    c = c + 1 #devera somar 1 até chegar a 10
#print('FIM')
#os dois programas tem o mesmo resultado


#quando voce nao sabe o limite
#n = 1
#while n != 0: #flag / ponto de parada / condicao de parada
#    n = int(input('Digite um valor: '))
#print('FIM')


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros PARES e {} numeros IMPARES '.format(par, impar))

