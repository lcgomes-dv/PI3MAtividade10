consumo_total = []
for x in range(1, 8):
    consumo_produto = int(input(f"Digite o consumo do produto {x}(em Kg): "))
    consumo_total.append(consumo_produto)

consumo_geral = sum(consumo_total)
produto_mais_consumido = max(consumo_total)
print(f"O consumo total dos 7 produtos é: {consumo_geral} Kg.")
print(f"O produto mais consumido é o produto {consumo_total.index(produto_mais_consumido) + 1} com {produto_mais_consumido} Kg.")
