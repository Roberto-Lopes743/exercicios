#quantas vezes vou querer rodar o sorteio
from random import randint
from time import sleep
repet = int(input('Quantos jogos de mega Sena gostaria de simular: '))
sorteio = []
lista = []
#fazer uma lista de numeros aleatorios entre 1 e 100 sem numeros 
for c in range(0,repet):
    for c2 in range(0,6):
        n = randint(0,60)
        if n in sorteio:
            repet+=1
        elif len(lista)==6:
            break
        else:
            lista.append(n)
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
for ind,l in enumerate(sorteio):
    print(f"Jogo {ind}: {l}")
    sleep(1)
print('Boa sote ♥')

