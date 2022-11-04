matriz = []

for colunas in range(3):
    linhas =  []
    for valor in range(0, 3, 1):
        nome = input("Insira seu nome: ")
        idade = input("Insira sua idade: ")
        cpf = input("Insira seu cpf: ")
        
        linhas.insert(valor, [nome, idade, cpf])
        break
    matriz.append(linhas)

for linhas in matriz:
    print(' '.join(map(str, linhas)))