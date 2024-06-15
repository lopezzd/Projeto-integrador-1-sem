from create    import *
from update    import *
from read      import *
from delete    import *
from simulação import *

while True:
    print("\n\nSTOCKPRIME")
    print("_"*50)
    print("Menu")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Procurar produto")
    print("4 - Atualizar produto")
    print("5 - Deletar produto")
    print("6 - Simular compra")
    print("7 - Encerrar")
    print("_"*50)
    try:
        Escolha = int(input("\nEscolha: "))
        if Escolha   == 1:
            cadastrar_produto()
        elif Escolha == 2:
            listar_produtos()
        elif Escolha == 3:
            procurar_produto()
        elif Escolha == 4:
            atualizar_produto()            
        elif Escolha == 5:
            excluir_produto()
        elif Escolha == 6:
            simular()
        elif Escolha == 7:
            print("Obrigado por usar!!!")
            break
    except ValueError:
        print("Valor errado, Insira novamente!")