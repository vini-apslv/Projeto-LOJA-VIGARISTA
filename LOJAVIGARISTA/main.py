import login
import menu_principal

def main():
    # 1. Faz o login uma única vez e guarda o resultado
    usuario = login.realizar_login()
    
    # 2. Verifica se o login deu certo usando a variável que já guardamos
    if usuario:
        print("\n" + "=" * 40)
        print("Acessando a Loja Vigarista...")
        print("=" * 40)
        print("\n[Sistema] Login realizado com sucesso!")
        
        # Abre o menu principal após a verificação de nome e idade
        menu_principal.exibir_menu()
    else:
        print("\nLogin falhou ou foi cancelado. Acesso negado.")

# Bloco de segurança: garante que o programa só rode se este arquivo for o principal
if __name__ == "__main__":
    main() 