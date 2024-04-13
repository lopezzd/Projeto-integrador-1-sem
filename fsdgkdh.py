try:
    custo_do_produto = float(input("Informe o custo do produto em reais: "))
    custo_administrativo = float(input("Informe o custo administrativo o produto em porcentagem: "))
    comissao_de_vendas = float(input("Informe a comissão de venda do produto em porcentagem: "))
    imposto = float(input("Informe os impostos em porcentagem: "))
    margem_de_lucro = float(input("Informe a margem de lucro desejada em porcentagem: "))
except ValueError:
    print("Informe o valor correto!!!")
preco_de_venda = custo_do_produto / ( 1 - ((((custo_administrativo)/100 + (comissao_de_vendas)/100 + (imposto)/100 + (margem_de_lucro)/100)/ 1 ))

print(preco_de_venda)