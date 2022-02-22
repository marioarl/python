#Dentro do pacote utilidadesCev que criamos no desafo111, temos o modulo chamado dado. Crie uma funcao
# chamada leiaDinheiro() que seja capaz de funcionar com a funcao input(), mas com uma validacao de dados
#para aceitar apenas valores que sejam monetarios.
from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço R$')
moeda.resumo(p, 25, 30)
