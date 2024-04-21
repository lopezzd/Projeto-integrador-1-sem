produtos_cadastrados = []
def cadastrar_usuario():
    try:
        nome_usuario = input("Informe  seu nome: ")
        tipo_usuario = int(input("Informe o tipo de usuário \n 1 - Administrador\n 2 - Consultador\n Insira: "))
        senha_usuario = input("Crie uma senha: ")
        confirmar_senha = input("Confirme sua senha: ")        
        
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
    except ValueError:
        print("Informe o valor correto!!!")
    preco_de_venda = custo_do_produto / ( 1 - (((custo_administrativo/100) + (comissao_de_vendas/100) + (imposto/100) + (margem_de_lucro/100)/ 1 )))
    print("O preço de venda de",nome_produto,"é de R$",preco_de_venda)
    produto_cadastrado = "Produto: ",nome_produto," de custo: ", preco_de_venda
    produtos_cadastrados.append(produto_cadastrado)

while True:
    print("STOCKPRIME")
    print("_"*25)
    print("Menu")
    print("1 - Cadastro de usuário")
    print("2 - Cadastrar preço")
    print("3 - Mostrar produtos cadastrados")
    print("4 - Encerrar")
    print("_"*25)
    try:
        Escolha = int(input("Escolha: "))

        if Escolha == 1:
            cadastrar_usuario()
            print("\n")
        elif Escolha == 2:
            preco_venda()
            print("\n")
        elif Escolha == 3:
            print("Produtos cadastrados")
            for i in range(len(produtos_cadastrados)):
                print(produtos_cadastrados[i])
            print("\n")
        elif Escolha == 4:
            print("Obrigado por usar!!!")
            break
        else:
            print("Insira um valor entre 1 e 4!!!\n")  
    except ValueError:
        print("Valor errado!")