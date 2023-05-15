'''
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu STATUS, de acordo com a tabela abaixo:
 - Abaixo de 18.5: Abaixo do peso
 - Entre 18.5 e 25: Peso ideal
 - 25 até 30: Sobrepeso
 - 30 até 40: Obesidade
 - Acima de 40: Obesidade Morbida
 '''

#Minha resposta
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal')
elif imc <= 25:
    print('PARABÉNS, voce está na faixa de PESO IDEAL')
elif imc <= 30:
    print('Voce está em SOBREPESO')
elif imc <= 40:
    print('Voce está em OBESIDADE!')
elif imc > 40:
    print('Voce está em OBESIDADE MORBIDA, CUIDADO!')

#resposta do Gustavo
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABENS, voce está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce está em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce está em OBESIDADE')
elif imc >= 40:
    print('Voce está em OBESIDADE MORBIDA, CUIDADO!')
