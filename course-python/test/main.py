
def romeu_e_julieta(value: int) -> str | int:
    """
        Param:
            value: int (number)
        Se value for divisível por 3 -> "Queijo"
        Se value for divisível por 5 -> "Goiabada"
        Se value for divisível por 3 e 5 -> "Romeu e Julieta'
        Se value não for divisível por 3 ou 5 -> value
    """
    # SUT = System Under Tests -> Função que irá ser testada 
    
    match value % 3 == 0, value % 5 == 0:
        case [True,False]:
            return "Queijo"
        case [False,True]:
            return "Goiabada"
        case [True,True]:
            return "Romeu e Julieta"
        case _:
            return value


