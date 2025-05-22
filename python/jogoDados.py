from random import randint
from operator import itemgetter
jogadores = {}
ranking = {}
for c in range(0,4):
    jogadores['jogador'+str(c+1)] = randint(1,6)
ranking = sorted(jogadores.items(), key=itemgetter(1))
for key,item in jogadores.items():
    print(f'{key} tirou {item}')
print('=-='*30)
print('=-= RANKING =-=')
for key,item in ranking:
    print(f'{key} tirou {item}')