def procurar_produto():
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Lop&s546",
        database = ""
    )

    mycursor = mydb.cursor()

    nome = input("Insira o nome do produto: ")
    sql = f"SELECT * FROM escola.stockprime WHERE nome_produto LIKE '%{nome}%'"
    
    mycursor.execute(sql)
    
    myresults = mycursor.fetchall()
        
    if(myresults):
        for i in myresults:
            print()
            print(f"Código do Produto..:{i[0]}")
            print(f"Nome do Produto....:{i[1]}")
            print(f"Desrição: {i[2]}")
            print(f"Preço de Venda.....:R${i[8]}  - {i[16]}%")
            print(f"Custo..............:R${i[3]}  - {i[17]}%")
            print(f"Receita Bruta......:R${i[9]}  - {i[18]}%")
            print(f"Custo Fixo.........:R${i[10]} - {i[19]}%")
            print(f"Comissão de Venda..:R${i[11]} - {i[20]}%")
            print(f"Imposto............:R${i[12]} - {i[21]}%")
            print(f"Outros gastos......:R${i[13]} - {i[22]}%")
            print(f"Rentabilidade......:R${i[14]} - {i[23]}%")
            print(f"A margem de lucro é: {i[15]}")
            print()

        print(f"Foram todos os resultados encontrados")
    else:
        print(f"Não foram encontrados nenhum item!")
    mydb.close()
        
def listar_produtos():
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Lop&s546",
        database = ""
    )

    mycursor = mydb.cursor()
    sql = f"SELECT * FROM escola.stockprime"
    
    mycursor.execute(sql)
    
    myresults = mycursor.fetchall()
    if(myresults):
        print(f"Lista de itens cadastrados:\n")
        for i in myresults:
            print(f"Nome do Produto....:{i[1]}\n")
        print()
    else:
        print(f"Não há itens cadastrados!\n")
    mydb.close()
    
def procurar_produto_sort(n):
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Lop&s546",
        database = ""
    )

    mycursor = mydb.cursor()
    
    sql = f"SELECT * FROM escola.stockprime WHERE nome_produto LIKE '%{n}%'"
    
    mycursor.execute(sql)
    myresults = mycursor.fetchall()
        
    if(myresults):
        for i in myresults:
            print()
            print(f"Nome do Produto....:{i[1]}")
            print(f"Desrição: {i[2]}")
            print(f"Custo..............:R${i[3]} ")
            print(f"Custo Fixo.........:R${i[4]}")
            print(f"Comissão de Venda..:R${i[5]}")
            print(f"Imposto............:R${i[6]}")
            print(f"Rentabilidade......:R${i[7]}\n")
            print()
    else:
        print(f"Não foram encontrados nenhum item!")
    mydb.close()