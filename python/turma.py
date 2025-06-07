def notas(*n, sit=True):
    n = list(n)
    media = sum(n)/len(n)
    maior = sorted(n)[-1]
    menor = sorted(n)[0]
    turma = {'media':media,'maior':maior,'menor':menor}
    if sit:
        if 3<media<=6:
            turma['situação'] = 'razoavel'
        elif 6<media<=10:
            turma['situação'] = 'incrivel'
        elif 6>media:
            turma['situação'] ='pessimo'
    return turma
print(notas(7,6,5,6,sit=False))