def introduction_page() -> str:
    message  : str = """
    1- Cadastrar pessoa
    2- Listar pessoas
    3-  Sair
    """

    print(message)
    command : str = input("Command: ")
    return command
