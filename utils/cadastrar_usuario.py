def cadastrar_usuario():
    try:
        nome_usuario = input("Informe  seu nome: ")
        tipo_usuario = int(input(": "))
        senha_usuario = input("Informe a comissão de venda do produto em porcentagem: ")
        confirmar_senha = input("Confirme sua senha: ")
        
    except ValueError:
        print("Informe o valor correto!!!")