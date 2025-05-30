from time import sleep
def cont(ini,fim,passo):
    cont = ini
    if passo ==0:
        passo =1
    if passo<0:
        passo*=-1
    if ini<=fim:
        while cont<=fim:
            print(cont, end=' ',flush=True)
            cont+=passo
            sleep(0.5)
    elif ini>=fim:
        while cont>=fim:
            print(cont, end=' ',flush=True)
            cont-=passo
            sleep(0.5)
    print('FIM')

cont(0,10,1)
cont(10,0,1)
cont(int(input('Inicio: ')),int(input('Final: ')),int(input('Passo: ')))

