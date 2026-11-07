
def exibir_menu():
    """Exibe o menu de opções da loja e gerencia a navegação do usuário."""
    while True:
        print("\n ┈┈┈┈ MENU ┈┈┈┈")
        print("1 - PRODUTOS")
        print("2 - MEU CARRINHO")
        print("6 - TROCAS/DEVOLUÇÕES")
        print("7 - ENTRAR EM CONTATO")
        print("0 - MEU PERFIL")
        print("0 - SAIR")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            print("Saindo...")
            break