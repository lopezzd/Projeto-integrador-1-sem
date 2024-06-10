from read import *
import mysql.connector


mydb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "Lop&s546",
  database = ""
)

mycursor = mydb.cursor()

def simular():
  id = input("insira o id do produto: ")
  dados = procurar_produto_sort(id)
  qtd = int("Informe a quantidade: ") 
  if qtd == 10:
    print("cu")
  else:
    print("Cu")