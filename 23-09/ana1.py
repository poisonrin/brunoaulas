user = input("Qual seu nome? ")
password = input("Qual a sua senha? ")

logado = False


def login (usuario, senha):
    global logado
    
    if usuario == "adm" and senha == "123":
        logado = True
        print("Bem Vindo!")
        
    else:
        print("Incorreto")
        
        
def logout ():
    global logado
    logado = False
    print("Até Mais!")


#Do while em python 3
while logado == False:
    login(user, password)
    if logado == True:
        break
    else:
        user = input("Qual seu nome? ")
        password = input("Qual a sua senha? ")