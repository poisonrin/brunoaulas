
def percorrer():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    cpf = int(input("Digite seu CPF: "))

    lista  = [nome, idade, cpf]
    print(lista)

    if not idade.replace('.', '').replace(',', '').isnumeric():
        print("Número Inválido")
    else: print("Ok")
        

percorrer()