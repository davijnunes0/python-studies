from .main import romeu_e_julieta

def test_romeu_e_julieta_deve_retornar_queijo():
    assert romeu_e_julieta(3) == "Queijo"

def test_romeu_e_julieta_deve_retornar_goiabada():
    value_input : int = 5
    expected_value : str = "Goiabada"
    result: str = romeu_e_julieta(value_input)
    assert result == expected_value


def test_romeu_e_julieta_deve_retornar_romeu_e_julieta():
    value_input : int = 15
    expected_value : str = "Romeu e Julieta"
    result : str = romeu_e_julieta(value_input)
    assert result == expected_value

def test_romeu_e_julieta_deve_retornar_value():
    value_input : int = 2
    expected_value : int = 2
    result : int = romeu_e_julieta(value_input)
    assert result == expected_value
