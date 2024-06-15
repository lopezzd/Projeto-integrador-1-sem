from read import *
import mysql.connector

def simular():
    mydb = mysql.connector.connect(
        host = "BD-ACD",
        user = "BD080324152",
        password = "Dnztb9",
        database = "BD080324152"
    )

    mycursor = mydb.cursor()

    n = 0
    compra = []
    valor_compra = 0
    resp = "S"
    total = 0
    while resp == "S":
      id = input("\nInsira o id do produto: ")

      sql = "SELECT * FROM stockprime WHERE id = %s"
      mycursor.execute(sql, (id,))
      myresults = mycursor.fetchall()

      if not myresults:
          print("Não foi encontrado nenhum item!")
      else:
          dados = myresults[0]
          
          qtd = int(input("Informe a quantidade: ")) 

          if qtd <= 0:
              print("Quantidade inválida")
          elif qtd > dados[-1]:
              print("Quantidade indisponível no estoque!")
          else:
              n += 1
              valor_unitario = dados[8]
              valor_total = valor_unitario * qtd
              item = f'\n{n}-{dados[1]}..............{qtd} x R${dados[8]:.2f}   R${valor_total:.2f}'
              compra.append(item)
              total += valor_total

              resp = input("Deseja continuar? [S/N]: ").upper()
      text = f'Total...................................R${total:.2f}'  
      compra.append(text)
      mycursor.close()
      mydb.close()





