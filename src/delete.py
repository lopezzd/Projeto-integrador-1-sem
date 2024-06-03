def excluir_produto():
    import mysql.connector

    mydb = mysql.connector.connect(
      host = "127.0.0.1",
      user = "root",
      password = "Lop&s546",
      database = ""
    )

    mycursor = mydb.cursor()
    try:
        id = input("Digite o código do produto que deseja excluir: ")
        sql = f"DELETE FROM escola.stockprime WHERE id = {id}"
        mycursor.execute(sql)
        
        mydb.commit()
        
        print("Produto excluído com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao excluir o produto: ", e)
    mydb.close()
