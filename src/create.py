def cadastrar_produto():
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Lop&s546",
        database = ""
    )

    mycursor = mydb.cursor()
    
    while True:
        try:
            nome_produto      = input("Informe o nome do produto: ")
            cp_valor          = float(input("Informe o custo do produto em reais: "))
            cf                = float(input("Informe o custo administrativo o produto em porcentagem: "))
            cv                = float(input("Informe a comissão de venda do produto em porcentagem: "))
            iv                = float(input("Informe os impostos em porcentagem: "))
            ml                = float(input("Informe a margem de lucro desejada em porcentagem: "))
            quantidade        = int(input("Informe a quantidade: "))
            descricao_produto = input("Informe a descrição: ")
            print("_"*50)
        except ValueError:
            print("Informe o valor correto!!!")
        
        preco_de_venda = cp_valor / ( 1 - (((cf/100) + (cv/100) + (iv/100) + (ml/100)/ 1 )))      
        
        lucro_percentual = ((preco_de_venda - cp_valor) / preco_de_venda) * 100
        
        if lucro_percentual > 20:
            lucro = f"Lucro alto"
        elif lucro_percentual <= 20 and lucro_percentual >= 10:
            lucro = f"Lucro médio"
        elif lucro_percentual <= 9 and lucro_percentual >= 1:
            lucro = f"Lucro baixo"
        elif lucro_percentual == 0:
            lucro = f"Sem lucro"
        else:
            print("Prejuízo \n")
        
        try:        
            sql = "INSERT INTO escola.stockprime ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro, quantidade)  VALUES ( %s,%s, %s,%s, %s,%s, %s, %s, %s)"
            valores = (nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro, quantidade)
            mycursor.execute(sql, valores)
            mydb.commit()
            print(f"Adicionado com sucesso! \n")
        except Exception as e:
            print("Ocorreu um erro ao excluir o produto: ", e)
        
        mydb.close()
        break