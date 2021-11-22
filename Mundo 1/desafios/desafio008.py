# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

# minha resposta
print('\033[1;33m(\033[m'*20, '\033[7;33mCONVERSOR DE MEDIDA\033[m', '\033[1;33m)\033[m'*20)
metros = float(input('\n\033[1;32mDigite o valor em metros: \033[m'))
print('\n\033[31mValor em centimetros:\033[m \033[1;30;41m{}cm\033[m\n\033[35mValor em milimetros:\033[m \033[1;45m{}mm\033[m'.format(metros * 100, metros * 1000))

# resposta do Gustavo
#medida = float(input('Uma distancia em metros: '))
#cm = medida * 100
#mm = medida * 1000
#print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))