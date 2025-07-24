from src.views.first_view  import introduction_page

def introduction_process() -> str:
    # Mostra a view para o usuário é retorna o comando selecionado pelo usuário
    command : str = introduction_page()
    # Retorna o comando selecionado pelo usuário
    return  command