matriz = []

def ingredientes():
    for colunas in range(1):
        linhas = []
        for i in range(0, 1, 1):
            ingrediente = input("Qual Ingrediente deseja adicionar? ")
            quantidade = int(input("Qual a quantidade? "))
            linhas.insert(i, [ingrediente, quantidade])
            break
        matriz.append(linhas)
        
    for linhas in matriz:
        print(' '.join(map(str, linhas)))
    
ingredientes()