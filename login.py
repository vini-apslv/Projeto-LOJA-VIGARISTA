def realizar_login():
    print("=" * 40)
    print("Seja muito bem-vindo(a) à LOJA VIGARISTA!😊")
    input("Pressione ENTER para começar...")
    print("=" * 40)
    
    # Coletando as informações do usuário
    nome = input("Digite o seu nome: ").strip().capitalize()
    
    # Validação simples para garantir que a idade seja um número
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")

    print("-" * 40)
    print(f"Perfeito, {nome}! Você está pronto para acessar a nossa loja.")
    input("Pressione ENTER para acessar...")
    
    # Retorna um dicionário com os dados para serem usados em outros arquivos
    return {
        "nome": nome,
        "idade": idade
    }