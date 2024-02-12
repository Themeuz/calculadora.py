custo_leite_condensado = 6.00
custo_granulado = 15.00
custo_chocolate_em_po = 30.00
custo_margarina = 13.00
custo_forma = 4.00
custo_casinha = 3.00

custo_total = (
    custo_leite_condensado +
    custo_granulado +
    custo_chocolate_em_po +
    custo_margarina +
    custo_forma +
    custo_casinha
)

preco_por_brigadeiro = 1.5
preco_por_venda = 3.50
lucro_por_brigadeiro = preco_por_venda - preco_por_brigadeiro
quantidade_brigadeiros = 8
lucro = lucro_por_brigadeiro * quantidade_brigadeiros
despesas_totais = custo_total * quantidade_brigadeiros

print(f"Custo total de um brigadeiro: R${custo_total:.2f}")
print(f"Lucro por brigadeiro: R${lucro_por_brigadeiro:.2f}")
print(f"Lucro total para {quantidade_brigadeiros} brigadeiros: R${lucro:.2f}")
print(f"Despesas totais para {quantidade_brigadeiros} brigadeiros: R${despesas_totais:.2f}")
