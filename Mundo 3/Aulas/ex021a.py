def teste():
	x=8
	print(f'Na função teste, n vale {n}') #mesmo o n sendo declarado abaixo, o n é igual a 2, pois o n está em um escopo GLOBAL 
	print(f'Na funcao teste, x vale {x}')

#programa principal
n =2
print(f'No programa principal, n vale {n}')
print(f'Na NO programa principal x vale {x}') #o programa irá dar um erro, pois o x foi declarado dentro de uma def, ela sá ira funcionar dentro da def, ou seja, um escopo local.

#funcoes com return
def somar(a=0, b=0, c=0):
	s = a + b + c
	return s


r1 = somar(3, 2, 5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados forma {r1}, {r2} e {r3}')
	


