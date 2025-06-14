def aumentar(n,q, moeda='R$:',formatado=True):
    """
    n = valor que   vai ser aumentado
    q =  porcentagem de aumento
    moeda = tipo monetario da região
    """
    n= n+(n*(q/100))
    if formatado:
       return f'{moeda}{n:.2f}'.replace('.',',')
    else:
        return n
def diminuir(n,q, moeda='R$:',formatado=True):
    """
    n = valor que   vai ser aumentado
    q =  porcentagem de aumento
    moeda = tipo monetario da região
    """
    n= n-(n*(q/100))
    if formatado:
       return f'{moeda}{n:.2f}'.replace('.',',')
    else:
        return n
def dobro(n, moeda='R$:',formatado=True):
    """
    n = valor que   vai ser aumentado
    moeda = tipo monetario da região
    """
    n= n*2
    if formatado:
       return f'{moeda}{n:.2f}'.replace('.',',')
    else:
        return n
def metade(n, moeda='R$:',formatado=True):
    """
    n = valor que   vai ser aumentado
    moeda = tipo monetario da região
    """
    n = n/2
    if formatado:
       return f'{moeda}{n:.2f}'.replace('.',',')
    else:
        return n
def resumo(n,t,formatado=True):
    if formatado:
        print(f'aumentando de R$:{n} em {t}% fica {aumentar(n,t)}')
        print(f'metade de R$:{n} fica {metade(n)}')
        print(f'o dobro de R$:{n} fica {dobro(n)}')
        print(f'diminuindo R$:{n} em {t}% fica {diminuir(n,t)}')
    else:
        Resumo = {}
        Resumo['metade'] = metade(n)
        Resumo['dobro'] = dobro(n)
        Resumo['aumento'] = aumentar(n,t)
        Resumo['diminuir'] = diminuir(n,t)
        return Resumo

