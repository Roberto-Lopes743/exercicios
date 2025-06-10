def aumentar(n,q):
    """
    n = valor que   vai ser aumentado
    q =  porcentagem de aumento
    """
    n= n+(n*(q/100))
    return n
def diminuir(n,q):
    """
    n = valor que   vai ser aumentado
    q =  porcentagem de aumento
    """
    n= n-(n*(q/100))
    return n
def dobro(n):
    n= n*2
    return n
def metade(n):
    n = n/2
    return n
print(aumentar(10,10))