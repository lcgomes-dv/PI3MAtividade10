n = int(input("Digite um número inteiro: "))
n_str = str(n)


for d in set(n_str):
    qtd = n_str.count(d)
    print(f"O dígito {d} aparece {qtd} vezes no número {n}.")