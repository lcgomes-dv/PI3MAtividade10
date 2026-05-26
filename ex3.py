valores = []
for x in range(1, 21): 
    n = float(input(f"Digite o número {x}: "))
    valores.append(n)

media = sum(valores) / len(valores)
print(f"A média dos números digitados é: {media}")