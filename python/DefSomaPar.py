from random import randint
def sortear(fim):
    lista = []
    for c in range(0,fim):
        num = randint(0,10)
        lista.append(num)
    return lista

def somarPares(lis):
    soma= 0
    for i in lis:
        if i%2==0:
            soma+=i
    return soma
lista = sortear(5)
print(lista)
print(somarPares(lista))