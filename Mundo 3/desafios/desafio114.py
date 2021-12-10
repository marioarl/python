#Crie um codigo em Python que teste se o site PUDIM está acessivel pelo computador.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim não está acessivel no momento')
else:
    print(f'Consegui acessar o site com suceso')

