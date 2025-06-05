def ficha(nome='',gols=''):
    if nome =='':
        return print('nome do jogador invalido')
    elif gols=='':
        return print('gols do jogador invalido')
    jogador = {'nome':nome,'gols':gols}
    return print(f'jogador {jogador["nome"]} fez {jogador["gols"]}')
print(ficha(input('digite o nome do jogador: '),input('digite quantos gols gols: ')))