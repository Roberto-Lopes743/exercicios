#Minha resolução
n = (int(input('Digite um numero maior que 1: ')))
if n>=1: #verifica se o numero e maior ou igual a 1
    if n%2==0:#verifica se o numero e par ou ímpar
        print(f'O numero {n} e par')
    else:
        print(f'O numero {n} e ímpar')
else:print('Digite um numero acima de 1')
#Minha resolução



#GPT
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro maior que 1: "))

# Garante que o número seja maior que 1
if numero <= 1:
    print("Por favor, digite um número maior que 1.")
else:
    eh_primo = True  # Assume que é primo até provar o contrário

    # Testa se existe algum divisor além de 1 e do próprio número
    for i in range(2, int(numero ** 0.5) + 1):  # Otimização: vai até a raiz quadrada do número
        if numero % i == 0:
            eh_primo = False
            break  # Encontrou um divisor, pode parar

    # Resultado final
    if eh_primo:
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} NÃO é um número primo.")
#GPT