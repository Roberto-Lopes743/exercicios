def aumentar(n,q, moeda='R$:'):
    """
    n = valor que   vai ser aumentado
    q =  porcentagem de aumento
    moeda = tipo monetario da região
    """
    n= n+(n*(q/100))
    return f'{moeda}{n:.2f}'
def diminuir(n,q, moeda='R$:'):
    """
    n = valor que   vai ser aumentado
    q =  porcentagem de aumento
    moeda = tipo monetario da região
    """
    n= n-(n*(q/100))
    return f'{moeda}{n:.2f}'.replace('.',',')
def dobro(n, moeda='R$:'):
    """
    n = valor que   vai ser aumentado
    moeda = tipo monetario da região
    """
    n= n*2
    return f'R$:{n:.2f}'.replace('.',',')
def metade(n, moeda='R$:'):
    """
    n = valor que   vai ser aumentado
    moeda = tipo monetario da região
    """
    n = n/2
    return f'{moeda}{n:.2f}'.replace('.',',')
