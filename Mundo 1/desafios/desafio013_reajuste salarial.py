'''
Faça um algoritimo que leia o salario de um funcionario e mostre seu novo
salario com 15% de aumento
'''

#Minha resposta
salario1 = float(input('Qual o salário do funcionário? R$'))
aumento = salario1 + (salario1 * 0.15)
print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario1, aumento))

#resposta do Gustavo
salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
