def excluir_produto():
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "BD-ACD",
        user = "BD080324152",
        password = "Dnztb9",
        database = "BD080324152"
    )

    mycursor = mydb.cursor()
    try:
        id = input("Digite o código do produto que deseja excluir: ")
        sql = f"DELETE FROM stockprime WHERE id = {id}"
        mycursor.execute(sql)
        
        mydb.commit()
        
        print("Produto excluído com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao excluir o produto: ", e)
    mydb.close()
