n1 = 0
n2 = 0

while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
    
        print(n1 + n2)
        break
    except:
        print("Digite um número válido.")