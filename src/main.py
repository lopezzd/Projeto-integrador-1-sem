from create import *
from update import *
from read   import *
from delete import *

                    
while True:
    print("STOCKPRIME")
    print("_"*50)
    print("Menu")
    print("1 - Cadastro de usuário")
    print("2 - Cadastrar produto")
    print("3 - Listar produtos")
    print("4 - Procurar produto")
    print("5 - Atualizar produto")
    print("6 - Deletar produto")
    print("7 - Encerrar")
    print("_"*50)
    try:
        Escolha = int(input("Escolha: "))
        if Escolha   == 1:
            print("Não implementado")
        elif Escolha == 2:
            cadastrar_produto()
        elif Escolha == 3:
            listar_produtos()
        elif Escolha == 4:
            procurar_produto()
        elif Escolha == 5:
            atualizar_produto()            
        elif Escolha == 6:
            excluir_produto()
        elif Escolha == 7:
            print("Obrigado por usar!!!")
            break
    except ValueError:
        print("Valor errado, Insira novamente!")