def vota(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual-ano
    if 0>idade:
        return print('valor incorreto')
    if idade >=18 and idade<=70:
        return f'com {idade} tem o voto obrigatorio'
    elif idade>=70 or 16<=idade<=17:
        return f'com {idade} anos tem o voto opcional'
    else:
        return f'com {idade} anos não pode votar'
print(f'pessoa: {vota(int(input('deigite sua data de nascimento: ')))}')