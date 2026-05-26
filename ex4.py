valores = []
for x in range(1, 6):
    n = float(input(f"Digite o número {x}: "))
    valores.append(n)

maior_num =  max(valores)
menor_num = min(valores)
media_num = sum(valores) / len(valores)
print(f"Maior número digitado: {maior_num}")
print(f"Menor número digitado: {menor_num}")
print(f"Média dos números digitados: {media_num}")