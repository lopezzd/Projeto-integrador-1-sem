import mysql.connector

mydb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "Lop&s546",
  database = ""
)

mycursor = mydb.cursor()

def atualizar_produto():
    while True:
      try:
          nome = int(input('Digite o código do produto: '))
          submenu = [\
                  '1 - Atualizar nome',\
                  '2 - Atualizar aniversário',\
                  '3 - Atualizar endereço',\
                  '4 - Atualizar telefone',\
                  '5 - Atualizar celular',\
                  '6 - Atualizar e-mail',\
                  '7 - Finalizar atualizações'\
                  ]
          
          escolha = int(opcaoEscolhida(submenu))  
          att_usuario = 0 
          
          if escolha == 1:
              att(nome, att_usuario, 'Nome...:', 0)
          if escolha == 2: 
              att(nome, att_usuario , 'Aniversario...: ', 1)
          if escolha == 3:
              att(nome, att_usuario, 'Endereco...:', 2)
          if escolha == 4:
              att(nome, att_usuario, 'Telefone...:', 3)
          if escolha == 5:
              att(nome, att_usuario, 'Celular...:', 4)
          if escolha == 6:
              att(nome, att_usuario, 'E-mail...:', 5)
          if escolha == 7:
              print(f'Atualizações finalizadas')
              break
      except ValueError:
        print("Por favor insira o código do número!")
