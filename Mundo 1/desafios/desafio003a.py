print ('\033[1;33m+\033[m'*10, '\033[1;46mSOMA DE NUMEROS\033[m', '\033[1;33m+\033[m'*10)
n1 = int(input('\033[1;36mDigite um numero:\033[m '))
n2 = int(input('\033[1;31mDigite outro numero:\033[m '))
s = n1 + n2
print('\033[1;33mA soma entre\033[m \033[1;36m{}\033[m e \033[1;31m{}\033[m é \033[1;37m{}'.format(n1, n2, s))