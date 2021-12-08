#Crie um pacote chamado utilidadesCev que tenha dois modulos internos chamados moeda e dado.
#Transfira todos as funcoes utilizadas nos desafios 107 até 110 para o primeiro pacote e mantenha tudo funcionando.
from ex111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p)
