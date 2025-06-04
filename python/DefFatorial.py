def fatorial(n,show=True):
    """
    -> n numero para fazer o fatorrial
    -> show para mostrar o calculo coompleto (True or False)
    """
    res = 1
    for c in range(n,0,-1):
        if show ==True:
            res= res*c
            print(f'{res} * {c} =',end='')
        else:
            res= res*c
    return res
print(fatorial(5))
help(fatorial)