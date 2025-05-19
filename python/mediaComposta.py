#pegar as informações do aluno
aluno = []
lista = []
c = 0
while True:
    nome = str(input('Aluno: '))
    nota = float(input(f'Nota do {nome}: '))
    nota2 = float(input(f'2° Nota do {nome} :'))
    lista.append(nome)
    lista.append(nota)
    lista.append(nota2)
    aluno.append(lista[:])
    lista.clear()
    #perguntar se vai continuar
    txt = str(input('continuar (s/n): ')).lower()
    if txt[0] == 'n':
        break
print('=-'*30)
print(f'{'ind':<4}|{'nome':<10}|{'media':<4}')
for ind,item in enumerate(aluno):
    print(f'{ind:<4}{item[0]:<10} {(item[1]+item[2])/2:<4}')
print('=-'*30)
while True:
    numAluno = int(input('qual aluno deseja ver as notas: '))
    print(f'aluno:{aluno[numAluno][0]}')
    print(f'1° nota:{aluno[numAluno][1]}')
    print(f'1° nota:{aluno[numAluno][2]}')
    txt = str(input('continuar (s/n): ')).lower()
    if txt[0] == 'n':
        break
    else:
        print('=-'*30)
        for ind,item in enumerate(aluno):
            print(f'{ind}     {item[0]} {(item[1]+item[2])/2}')
        print('=-'*30)
print('FINALIZADO')