# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo
#salario com 15% de aumento

#minha resposta
#salario = float(input('Qual o salário do funcionário? R$'))
#aumento = salario + (salario * 0.15)
#print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))

#resposta do Gustavo
salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
