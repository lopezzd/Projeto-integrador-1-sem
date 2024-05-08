from utils import *
                    
while True:
    print("STOCKPRIME")
    print("_"*50)
    print("Menu")
    print("1 - Cadastro de usuário")
    print("2 - Cadastrar produto")
    print("3 - Encerrar")
    print("_"*50)
    try:
        Escolha = int(input("Escolha: "))
        if Escolha == 1:
            cadastrar_usuario()
        elif Escolha == 2:
            cadastrar_produto()
        elif Escolha == 3:
            print("Obrigado por usar!!!")
            break
    except ValueError:
        print("Valor errado!")