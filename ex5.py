n = int(input("Digite um número inteiro positivo: "))
n_str = str(n)
cont = 0

for digito in n_str:
    cont += 1
    
print(f"O número {n} possui {cont} dígitos.")
