'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados'''

#minha resposta
print('\033[1;36m=\033[m' * 10, '\033[1;7;35mQUANTIDADE DE TINTA\033[m', '\033[1;36m=\033[m' * 10)
l = float(input('\033[33mLargura da parede em metros:\033[m '))
a = float(input('\033[34mAltura da parede em metros:\033[m '))
area = a * l
tinta = area / 2
print('\n\033[31mSua parede tem dimensão de {:.2f} X {:.2f} e sua área é de\033[m \033[7;31m{:.2f}m2\033[m'.format(l, a, area))
print('\033[33mPara pintar essa parede, voce precisará de\033[m \033[7;33m{:.2f}'.format(tinta),('l de tinta\033[m'))

#resposta do Gustavo
#larg = float(input('largura da parede: '))
#alt = float(input('Altura da parede: '))
#area = larg * alt
#print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg, alt, area))
#tinta = area / 2
#print('Para pintar essa parede, voce precisará de {}l de tinta'.format (tinta))