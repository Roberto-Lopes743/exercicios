import datetime
ano = datetime.datetime.now().today().year
funcionario = {}
funcionario['nome'] = str(input('Digite o nome do funcionario: '))
funcionario['idade'] = ano-int(input(f'Digite o ano de nascimento do {funcionario["nome"]}: '))
funcionario['carteira'] = int(input('Carteira de trabalho(digite 0 caso não há): '))
if funcionario['carteira'] !=0:
    funcionario['contrato'] = int(input(f'Qual ano o {funcionario["nome"]} foi contratado: '))
    funcionario['salario'] = float(input(f'salario do {funcionario["nome"]}: '))
funcionario['aposentadoria']= (funcionario['contrato']+35)-(ano-funcionario['idade'])
for ind, item in funcionario.items():
    print(f'{ind} = {item}')
print(f'vai se aposentar com {funcionario["aposentadoria"]} anos em {funcionario['contrato']+35}')