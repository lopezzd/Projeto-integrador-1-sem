def cadastrar_usuario():
    try:
        nome_usuario = input("Informe  seu nome: ")
        tipo_usuario = int(input("Informe o tipo de usuário \n 1 - Administrador\n 2 - Consultador\n Insira: "))
        senha_usuario = input("Crie uma senha: ")
        confirmar_senha = input("Confirme sua senha: ")
        print("\n")        
        
    except ValueError:
        print("Informe o valor correto!!!")
        
def preco_venda():
    try:
        nome_produto = input("Informe o nome do produto: ")
        custo_do_produto = float(input("Informe o custo do produto em reais: "))
        custo_administrativo = float(input("Informe o custo administrativo o produto em porcentagem: "))
        comissao_de_vendas = float(input("Informe a comissão de venda do produto em porcentagem: "))
        imposto = float(input("Informe os impostos em porcentagem: "))
        margem_de_lucro = float(input("Informe a margem de lucro desejada em porcentagem: "))
        print("_"*50)
    except ValueError:
        print("Informe o valor correto!!!")
    preco_de_venda = custo_do_produto / ( 1 - (((custo_administrativo/100) + (comissao_de_vendas/100) + (imposto/100) + (margem_de_lucro/100)/ 1 )))
    
    print("\n")
    print("_"*50)
    print(f"Tabela de calculos de {nome_produto}")
    print("_"*50)    
    print(f"A - Preço de venda é {preco_de_venda} ")
    print(f"B - Custo de Aquisição é {custo_do_produto}")
    print(f"C - Receita Bruta é {preco_de_venda - custo_do_produto}")
    print(f"D - Custo Fixo é {(preco_de_venda)*(custo_administrativo/100)}")
    print(f"E - Comissa de Vendas é {(preco_de_venda)*(comissao_de_vendas/100)}")
    print(f"F - Impostos é {(preco_de_venda)*(imposto/100)}")
    print(f"G- Outros Custos é {(preco_de_venda)*(imposto/100)}")
    print(f"H - Rentabilidade é {(preco_de_venda)*(margem_de_lucro/100)}")
    
    lucro_percentual = ((preco_de_venda - custo_do_produto) / preco_de_venda) * 100
    if lucro_percentual > 20:
        print("Lucro alto")
    elif lucro_percentual <= 20 and lucro_percentual >= 10:
        print("Lucro médio")
    elif lucro_percentual <= 9 and lucro_percentual >= 1:
        print("Lucro baixo")
    elif lucro_percentual == 0:
        print("Sem lucro")
    else:
        print("Prejuízo")
    print("_"*50)
    print("\n")
    