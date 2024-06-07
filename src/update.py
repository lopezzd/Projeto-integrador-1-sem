from read import *
import mysql.connector

mydb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "Lop&s546",
  database = ""
)

mycursor = mydb.cursor()

def atualizar_produto():
    nome = input("Insira nome do produto: ")
    procurar_produto_sort(nome)          
    submenu = [\
            '1 - Atualizar nome.',\
            '2 - Atualizar descrição.',\
            '3 - Atualizar custo.',\
            '4 - Atualizar custo fixo.',\
            '5 - Atualizar comissão de venda.',\
            '6 - Atualizar impostos.',\
            '7 - Finalizar rentabilidade.'\
            ]
    for i in submenu:
        print(i)
    escolha = int(input('Escolha: '))  
    
    while True:
        if escolha == 1:
            alteracao = input("Insira o nome novo:")
            sql = f"""UPDATE stockprime SET nome = '{alteracao}' WHERE nome_produto = {nome};"""
            mycursor.execute(sql)
            mydb.close() 
            break
        elif escolha == 2: 
            alteracao = input("Insira a descrição nova:")
            sql = f"""UPDATE escola.stockprime SET descricao_produto = '{alteracao}' WHERE nome_produto = '{nome}';"""
            mycursor.execute(sql)
            mydb.close() 
            break
        elif escolha == 3:
            alteracao = input("Insira o custo novo:")
            sql = f"""UPDATE stockprime SET cp_valor = '{alteracao}' WHERE nome_produto = {nome};"""
            mycursor.execute(sql)
            mydb.close() 
            break
        elif escolha == 4:
            alteracao = input("Insira o custo fixo novo:")
            sql = f"""UPDATE stockprime SET cf = '{alteracao}' WHERE nome_produto = {nome};"""
            mycursor.execute(sql)
            mydb.close() 
            break
        elif escolha == 5:
            alteracao = input("Insira comissão de venda nova:")
            sql = f"""UPDATE stockprime SET cv = '{alteracao}' WHERE nome_produto = {nome};"""
            mycursor.execute(sql)
            mydb.close() 
            break
        elif escolha == 6:
            alteracao = input("Insira o imposto novo:")
            sql = f"""UPDATE stockprime SET iv = '{alteracao}' WHERE nome_produto = {nome};"""
            mycursor.execute(sql)
            mydb.close() 
            break
        elif escolha == 7:
            alteracao = input("Insira a rentabilidade nova:")
            sql = f"""UPDATE stockprime SET ml = '{alteracao}' WHERE nome_produto = {nome};"""
            mycursor.execute(sql)
            mydb.close()  
            break
        else:
            print(f'Escolha incorreta!')
  
