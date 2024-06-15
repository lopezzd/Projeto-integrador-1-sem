from read import *
import mysql.connector

mydb = mysql.connector.connect(
    host = "BD-ACD",
    user = "BD080324152",
    password = "Dnztb9",
    database = "BD080324152"
)

mycursor = mydb.cursor()

def atualizar_produto():
    id = int(input("Insira ID do produto: "))
    procurar_produto_sort(id)          
    submenu = [\
            '1 - Atualizar nome.',\
            '2 - Atualizar descrição.',\
            '3 - Atualizar custo.',\
            '4 - Atualizar custo fixo.',\
            '5 - Atualizar comissão de venda.',\
            '6 - Atualizar impostos.',\
            '7 - Atualizar rentabileade.'\
            '8 - Voltar'
            ]
    for i in submenu:
        print(i)
    escolha = int(input('Escolha: '))  
    
    while True:
        if escolha == 1:
            alteracao = input("Insira o nome novo:")
            sql = """UPDATE stockprime SET nome = %s WHERE e = %s\
                                        SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
                """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit() 
            break
        elif escolha == 2: 
            alteracao = input("Insira a descrição nova: ")
            sql = """UPDATE stockprime SET descricao_produto = %s WHERE id = %s\
                                        SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
            """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit() 
            break
        elif escolha == 3:
            alteracao = input("Insira o custo novo:")
            sql = """UPDATE stockprime SET cp_valor = %s WHERE id = %s\
                                        SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
            """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit() 
            break
        elif escolha == 4:
            alteracao = input("Insira o custo fixo novo:")
            sql = """UPDATE stockprime SET cf = %s WHERE id = %s\
                                        SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
                """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit() 
            break
        elif escolha == 5:
            alteracao = input("Insira comissão de venda nova: ")
            sql = """UPDATE stockprime SET cv = %s WHERE id = %s;\
                            SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
            """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit() 
            break
        elif escolha == 6:
            alteracao = input("Insira o imposto novo:")
            sql = """UPDATE stockprime SET iv = %s WHERE id = %s;\
                            SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
                """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit() 
            break
        elif escolha == 7:
            alteracao = input("Insira a rentabilidade nova: ")
            sql = """UPDATE stockprime SET ml = %s WHERE id = %s;\
                SET lucro = \
                    CASE \
                        WHEN lc_porc > 20 THEN 'Lucro alto'\
                        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'\
                        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'\
                        WHEN lc_porc = 0 THEN 'Lucro baixo'\
                        ELSE 'Sem lucro'\
                    END;\
            """
            mycursor.execute(sql, (alteracao, id))
            mydb.commit()  
            break
        elif escolha == 8:
            break
        else:
            print(f'Escolha incorreta!')
  
