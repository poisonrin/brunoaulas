#matriz = [[1,2], [4,5]]

#for i in matriz:
    #print(' '.join(map(str, i)))
#print(matriz)

matriz = []

for colunas in range(3):
    linhas =  []
    for valor in range(3):
        nome = input("Insira seu nome: ")
        linhas.append(nome)
        idade = input("Insira sua idade: ")
        linhas.append(idade)
        cpf = input("Insira seu cpf: ")
        linhas.append(cpf)
        break
    matriz.append(linhas)

for linhas in matriz:
    print(' '.join(map(str, linhas)))