vendas = []
for x in range(1, 7):
    valor = float(input(f"Digite o valor da venda referente a {x}/6: "))
    vendas.append(valor)

total_vendas = sum(vendas)
media_vendas = total_vendas / len(vendas)

meses_acima = 0
for venda in vendas:
    if venda > media_vendas:
        meses_acima += 1
        
print(f"Total de vendas: R$ {total_vendas}")
print(f"Média de vendas: R$ {media_vendas}")
print(f"Meses acima da média: {meses_acima}")