aluno = {}
aluno['nome'] = str(input('digite o nome do aluno: '))
aluno['media'] = float(input('digite a media do aluno: '))

print('=-='*30)
if aluno['media'] <6:
    aluno['stats'] = 'reprovado'
elif aluno['media'] ==6:
    aluno['stats'] = 'recuperação'
else:
    aluno['stats'] = 'aprovado'
for k,v in aluno.items():
    print(f'{k} = {v}')
print('=-='*30)