n = int(input("Digite um número inteiro: "))
multiplo = 1
for i in range(1, 11):
    multiplo = n * i
    print(f"{n} x {i} = {multiplo}")