def cadastrar(nome='',idade=''):
    """
    Adiciona um novo usuário com nome e idade.

    Args:
        nome (str): Nome do usuário.
        idade (int): Idade do usuário.
        lista (list): Lista onde o usuário será adicionado.
    Returns:
        str: Mensagem de confirmação.
    """
    if nome == '' or idade == '':
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
    with open('cadastrados.txt', 'a') as file:
        file.write(f"{nome:30} {idade:3} anos\n")
def listar(lista):
    """
    Lista todos os usuários cadastrados.

    Args:
        lista (list): Lista de usuários.
    Returns:
        list: Lista de usuários.
    """
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
def menu(*args):
    """
    Exibe as opções disponíveis para o usuário.

    Returns:
        str: Opção escolhida pelo usuário.
    """
    for index,item in enumerate(args):
        print(f'{index+1} - {item}')
    print('-=-'*30)
def continuar():
    cont = input("Deseja cadastrar mais alguém? (s/n): ").lower()[0]
    while cont not in 'sn':
        cont = input("error, tente novamente. Deseja cadastrar mais alguém? (s/n): ").lower()[0]
    if cont == 's':
        return True 
    elif cont == 'n':
        return False
def verificarArquivo(criar=False):
    """
    Verifica se o arquivo do cadastro existe.
    criar (bool): Se True, cria o arquivo se não existir.
    Returns:
        bool: Retorna True se o arquivo existe, False caso contrário.
    """
    try:
        with open('cadastrados.txt', 'r') as file:
            return True
    except FileNotFoundError:
        if criar:
            with open('cadastrados.txt', 'w') as file:
                file.write(f"{'       Usuários cadastrados:':}\n")
                file.write(f"{"nome":30} {"idade":3}\n")
                file.write(f"{'---'*30}\n")
                pass
        return False
def escolher_opcao():
    opcao = input("Digite a opção: ")
    while opcao.isnumeric()== False:
        print("Opção inválida. Tente novamente.")
        opcao = input("Digite a opção: ")
    return opcao
def sistema(tabela=True):
    verificarArquivo(True)
    pessoas_cadastradas = open('cadastrados.txt', 'r')
    while True:
        if tabela:
            menu('Cadastrar usuário', 'Listar usuários', 'Sair')
            opcao = escolher_opcao()
        if opcao == '1':
            while True:
                cadastrar(pessoas_cadastradas)
                if continuar():
                    continue
                else:

                    print('-=-'*30)
                    print("Cadastro concluído.")
                    print('-=-'*30)
                    break
        elif opcao == '2':
            print('-=-'*30)
            if pessoas_cadastradas:
                with open('cadastrados.txt', 'r') as file:
                    print(file.read())
                print('-=-'*30)
            else:
                print("Nenhum usuário foi cadastrado.")
        elif opcao == '3':
            print("Saindo do programa...")
            break