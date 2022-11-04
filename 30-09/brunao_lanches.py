def inicio():
    print('-' * 37)
    print('------------BRUNAO LANCHES-----------')
    print('-' * 37)
    print('')
usuario = ''
senha = ''
cliente = ''

def cadastrar():
    global usuario
    global senha
    usuario = input("Crie seu usuário: ")
    senha = input("Crie sua senha: ")
    print('-' * 30)

def menu():
    print('')
    print('-' * 30)
    print("Seu Usuário é: " + usuario) 
    print("Sua senha é: " + senha)
    print("(1)Editar Usuário")
    print("(2)Editar senha")
    print("(3)Excluir")
    print("(4)Sair")
    print("(5)Clientes")
    print("(6)Estoque")
    acao()

def excluir():
    global usuario
    global senha
    usuario = ''
    senha = ''

def alterarSenha():
    global senha
    senha = input("Digite sua nova senha: ")

def alterarUsuario():
    global usuario
    usuario = input("Digite seu novo usuario: ")

global Ingredientes
Ingredientes = []

def estoque():
    if Ingredientes == []:
        print("Ingredientes no estoque:",Ingredientes)
        acao = input("Adicionar ingredientes?(1-Sim 2-Não): ")
        if acao == '1':
            CreateIngredientes()
        elif acao == '2':
            menu()
    else:
        print('-' * 100)
        print("Ingredientes atualmente no estoque:",Ingredientes)
        print("Escolha a sua ação, ademir.")
        print("(1) Adicionar ingredientes")
        print("(2) Quantidade de ingredientes")
        print("(3) Excluir ingredientes")
        print("(4) Sair")
        acao = input("O que deseja fazer?: ")
        if acao == '1':
            CreateIngredientes()
        elif acao == '2':
            quantIng()
        elif acao == '3':
            deletar()
        elif acao == '4':
            menu()
        else:
            ("algo deu errado amigão, vamo voltar")
            estoque()
global valor
def quantIng():

    print("Ingredientes sem a Quantidade.")
    for i in Ingredientes:
        print(i)
    nome = input("Escreva o ingrediente que deseja adicionar:")
    for i in Ingredientes:
        if nome == i:
            valor = str(input("Quantidade de ingredientes para adicionar no estoque: "))
            for i in Ingredientes:
                if i == nome:
                    print(i,"-",valor)
                    #infelizmente não consegui fazer isso no puro python, iria realmente precisar do banco de dados :(
                    estoque()
                else:
                    print(i)

def deletar():
    delet = input("Escreva o nome do ingrediente para excluir: ")
    for i in Ingredientes:
        if delet == i:
            Ingredientes.remove(delet)
            estoque()
        else:
            deletar()

def CreateIngredientes():

    NIngredientes = int(input("Quantos Ingredientes deseja adicionar? "))

    for i in range (NIngredientes):
        Valor = input("Qual ingrediente deseja adicionar? ")
        global Ingredientes
        Ingredientes.append(Valor)

    print("Os ingredientes adicionados foram: ", Ingredientes)
    estoque()

def acao(): 
    acao = input("Digite o número do que quer fazer: ")

    if acao == '1':
        print("Você vai editar seu usuário")
        alterarUsuario()
        print("Seu usuário atual é: " + usuario)
        menu()
    elif acao == '2':
        print("Deseja editar sua senha?")
        alterarSenha()
        print("Sua senha atual é: "+ senha)
        menu()
    elif acao == '3':
        print("Deseja excluir tudo?")
        excluir()
        print("Seu usuario foi excluido")
        cadastrar()
        menu()
    elif acao == '4':
        inicio()
    elif acao == '5':
        clientes()
    elif acao == '6':
        estoque()
    else:
        print("ocorreu um erro, a aplicação deverá parar.")
        inicio()

def login():
    teste = bool(False) 
    teste2 = bool(False)
    print('-' * 30)
    print("Hora de fazer o login!")
    usuarioLocal = input("Usuário: ")
    senhaLocal = input("Senha: ")
    if usuarioLocal == usuario:
        teste = True
    else:
        teste = False
        print("Seu Usuário está incorreto")
    if senhaLocal == senha:
        teste2 = True
    else:
        teste2 = False
        print("Sua Senha está incorreta")

    if teste2 and teste == True:
        print("Login feito com sucesso!")
        menu()
    else:
        print("Ocorreu um erro")
        login()

cliente = []

def clientes ():
    if cliente == []:
        NClientes = int(input("Quantos Clientes deseja adicionar? "))

        for i in range (NClientes):
                cli = input("Qual o nome do cliente? ")
                
                cliente.append(cli)

        print("O nome dos clientes são: ", cliente)
        print("(1)Editar o cliente")
        print("(2)Sair")
        acao = input("O que deseja fazer?")
        if acao == '1':
            print("Qual cliente você quer editar?")
            for i in cliente:
                print(i)
            nome = input("Digite o nome do cliente:")
            for i in cliente:
                if nome == i:
                    global sobrenome
                    sobrenome = input("Digite o sobrenome:")
                    global compra
                    compra = input("O que comprou:")
                    clientes()
        elif acao == '2':
            menu()
        else:
            "Ocorreu um erro"
            clientes()
    else:
        print(cliente)
        print("(1)Deseja voltar?")
        print("(2)Veja o cliente")
        acao = input("O que deseja fazer?:")
        if acao == '1':
            menu()
        elif acao == '2':
            for i in cliente:
                print("Escolha entre um dos clientes:")
                print(i)
                nome = input("Digite o nome do cliente:")
                for i in cliente:
                    if nome == i:
                        print(i)
                        print(sobrenome)
                        print(compra)
                    else:
                        clientes()
        else:
            clientes()
inicio()
cadastrar()
login()