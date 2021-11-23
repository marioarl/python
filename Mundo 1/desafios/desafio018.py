# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno \
# e tangente desse angulo

#minha resposta 1 (as funcoes sin, cos e tan funcionam com radioano
from math import sin, cos, tan, radians
ang = float(input('Digite o angulo que voce deseja: '))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ang, sin))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(ang, tan))