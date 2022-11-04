n1 = input("Digite um número: ")

if not n1.replace('.', '').replace(',', '').isnumeric():
    print("Número Inválido")
else: print("Ok")