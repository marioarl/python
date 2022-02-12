def lin30():
    print('-=' * 30)


a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

lin30()

def soma(a, b):
    s = a + b
    print(s)


#programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

lin30()
soma(a=4, b=5)

lin30()
soma(b=4, a=5) #pode tambem trocar os parametros

lin30()
def somb(a, b):
    print(f'A = {a} e B = {b}')
    s = a+ b
    print(f'A soma A + B = {s}')


somb(b=4, a=5)

lin30()
def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

lin30()
def contador1(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


contador1(2, 1, 7)
contador1(8, 0)
contador1(4, 4, 7, 6, 2)
