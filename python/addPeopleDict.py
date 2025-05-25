pessoas = []
pessoa = {}
media = 0
Flist = 0
aciM = 0
while True:
    name = str(input('digite o nome: '))
    sex = str(input('digite o sexo(M/F): ')).upper()
    while sex != 'M' and sex != 'F':
        sex = str(input('Valor invalido digite o sexo(M/F): ')).upper()
    if sex =='F':
        Flist+=1
    year = int(input('digite sua idade: '))
    pessoa['nome'] = name
    pessoa['sexo'] = sex
    pessoa['idade'] = year
    media +=year
    pessoas.append(pessoa.copy())
    end = str(input('deseja continuar (S/N): ')).lower()
    while end != 's' and end !='n':
        end = str(input('Valor invalido. Deseja continuar (S/N): ')).lower()
    if end[0] == 'n':
        break
    pessoa.clear()
media/=len(pessoas)
for i in pessoas:
    if i['idade'] >media:
        aciM +=1
print('=-='*30)
print(f'foram cadastradas {len(pessoas)} pessoas')
print(f'media das idades foi de {media:.2f}')
for i in pessoas:
    if i['sexo'] == 'F':
        print(i['nome'])
print(f'temos {Flist} mulheres')
print(f'temos {aciM} pessoas com idade acima da media')