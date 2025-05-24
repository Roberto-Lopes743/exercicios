jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input('Quantos partidas: '))
gols = []
tot = 0
for i in  range(0,jogador['partidas']):
    gol =int(input(f'Quantos gols na partida {i+1}°: '))
    gols.append(gol)
    jogador['gols'] = gols
jogador['totGols'] = sum(jogador['gols'])
for k,i in jogador.items():
    print(f'{k} = {i}')